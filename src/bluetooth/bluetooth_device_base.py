import datetime
import logging

from PySide6.QtBluetooth import QLowEnergyController, QLowEnergyService, QBluetoothDeviceInfo, QLowEnergyCharacteristic, \
    QBluetoothUuid
from PySide6.QtCore import QObject, QByteArray, Signal, QTimer
from typing import Union, List

from src.appdata import AppDataPaths
from src.bluetooth.bluetooth_utils import BluetoothUtils
from src.settings import Settings


class BluetoothDeviceBase(QObject):
    """
    Connect to a device that acts as a Bluetooth server / peripheral.
    On Windows, the sensor must already be paired with the machine running
    the app. Pairing isn't implemented in Qt6.

    In Qt terminology client=central, server=peripheral.
    """

    error = Signal(str)
    disconnecting = Signal(str)
    disconnected = Signal(str)
    connecting = Signal(str)
    connected = Signal(str)
    status_update = Signal(str, str)
    rssi_read = Signal(int)
    do_authenticate = Signal()

    def __init__(self, device: QBluetoothDeviceInfo, 
                 service_uuid: QBluetoothUuid, 
                 heartbeat_interval: int,
                 device_heartbeat_interval: int) -> None:
        super().__init__()
        self._ble_device = device
        self._controller: Union[None, QLowEnergyController] = None
        self._service: Union[None, QLowEnergyService] = None
        self._service_uuid: QBluetoothUuid = service_uuid
        self._notification_uuids: List[QBluetoothUuid] = []
        self._notifications = []
        self.ENABLE_NOTIFICATION: QByteArray = QByteArray.fromHex(b"0100")
        self.DISABLE_NOTIFICATION: QByteArray = QByteArray.fromHex(b"0000")
        self._heartbeat_timer = QTimer()
        self._heartbeat_timer.setInterval(heartbeat_interval)
        self._heartbeat_timer.timeout.connect(self._heartbeat)
        self._device_heartbeat_interval = device_heartbeat_interval
        self._set_next_expected_heartbeat()
        self._app_paths = AppDataPaths('mlm2pro-gspro-connect')
        self._settings = Settings(self._app_paths)

        #self.hr_notification: Union[None, QLowEnergyDescriptor] = None
        #self._service: QBluetoothUuid.ServiceClassUuid = (
        #    QBluetoothUuid.ServiceClassUuid.HeartRate
        #)
        #self.HR_CHARACTERISTIC: QBluetoothUuid.CharacteristicType = (
        #    QBluetoothUuid.CharacteristicType.HeartRateMeasurement
        #)

    def _sensor_address(self):
        return self._controller.remoteAddress().toString()

    def connect_device(self):
        if self._ble_device is None:
            self.error.emit("No device to connect to.")
            return
        print(f'connect_client {self._ble_device.name()}')
        if self._controller is not None:
            logging.debug(f"Currently connected to {self._ble_device.name()} at {self._ble_device.remoteAddress().toString()}.")
            self.connected.emit('Connected')
            return
        print(f'Connecting to {self._ble_device.name()}')
        self.status_update.emit('Connecting...', self._ble_device.name())
        self._controller = QLowEnergyController.createCentral(self._ble_device)
        self._controller.setRemoteAddressType(QLowEnergyController.RemoteAddressType.PublicAddress)
        self._controller.errorOccurred.connect(self.__catch_error)
        self._controller.connected.connect(self.__discover_services)
        self._controller.rssiRead.connect(self.__rssi_read)
        self._controller.serviceDiscovered.connect(self.__service_found)
        self._controller.discoveryFinished.connect(self.__connect_to_service)
        self._controller.disconnected.connect(self.__reset_connection)
        #self._controller.rssiRead.connect(self.__rssi_read)
        self._controller.connectToDevice()

    def __rssi_read(self, rssi: int):
        self.rssi_read.emit(rssi)

    def __service_found(self, service_uuid: QBluetoothUuid):
        logging.debug(f'Found service: {service_uuid.toString()}')
        print(f'Found service: {service_uuid.toString()}')
        
    def _heartbeat(self):
        pass

    def disconnect_device(self):
        print(f'self._notifications: {self._notifications}')
        if len(self._notifications) > 0 and self._service is not None:
            logging.debug('Unsubscribing from notifications')
            print('Unsubscribing from notifications')
            for notification in self._notifications:
                if not notification.isValid():
                    self._service.writeDescriptor(notification, self.DISABLE_NOTIFICATION)
        if self._ble_device is not None:
            logging.debug(f'Disconnecting from device: {self._ble_device.name()}')
        if self._heartbeat_timer.isActive():
            self._heartbeat_timer.stop()
        if self._controller is not None:
            self.disconnecting.emit('Disconnecting...')
            self._controller.disconnectFromDevice()


    def __discover_services(self):
        print(f'discover services state: {self._controller.state()}')
        if self._controller is not None:
            logging.debug(f'Discovering services for {self._ble_device.name()}')
            self.status_update.emit('Discovering services...', self._ble_device.name())
            self._controller.discoverServices()

    def __connect_to_service(self):
        self.status_update.emit('Connecting to service...', self._ble_device.name())
        print(f'__connect_to_service {self._controller.services()}')
        primary_service: list[QBluetoothUuid] = [
            s for s in self._controller.services() if self._service_uuid.toString().upper() in s.toString().upper()
        ]
        if not primary_service:
            msg = f"Could not find primary service on {self._sensor_address()}."
            logging.debug(msg)
            self.error.emit(msg)
            return
        logging.debug(f'Connecting to service {primary_service[0].toString()} on {self._sensor_address()}')
        self._service = self._controller.createServiceObject(primary_service[0])
        if not self._service:
            msg = f"Couldn't establish connection to HR service on {self._sensor_address()}."
            logging.debug(msg)
            self.error.emit(msg)
            return
        logging.debug(f'Connected to service {self._service.serviceUuid().toString()} on {self._sensor_address()}')
        self._service.stateChanged.connect(self._subscribe_to_notifications)
        self._service.characteristicChanged.connect(self._data_handler)
        self.do_authenticate.connect(self._authenticate)
        print(f'Discovering service details {self._service.serviceUuid().toString()} on {self._sensor_address()}')
        logging.debug(f'Discovering service details {self._service.serviceUuid().toString()} on {self._sensor_address()}')
        self._service.discoverDetails()

    def _subscribe_to_notifications(self, state: QLowEnergyService.ServiceState):
        self.status_update.emit('Subscribing...', self._ble_device.name())
        if state != QLowEnergyService.ServiceState.RemoteServiceDiscovered:
            return
        if self._service is None:
            return
        for uuid in self._notification_uuids:
            msg = f"Subscribing to notifications for {uuid.toString()} on {self._sensor_address()}."
            logging.debug(msg)
            print(msg)
            characteristic = self._service.characteristic(uuid)
            if not characteristic.isValid():
                msg = f"Couldn't find characteristic {uuid.toString()} on {self._sensor_address()}."
                logging.debug(msg)
                self.error.emit(msg)
                return
            # Get the descriptor for client characteristic configuration
            descriptor = characteristic.descriptor(
                QBluetoothUuid.DescriptorType.ClientCharacteristicConfiguration
            )
            if not descriptor.isValid():
                msg = f"Characteristic descriptor is invalid for {uuid.toString()} on {self._ble_device.remoteAddress().toString()}."
                logging.debug(msg)
                self.error.emit(msg)
                return
            self._notifications.append(descriptor)
            # Subscribe to notifications for the characteristic
            self._service.writeDescriptor(descriptor, self.ENABLE_NOTIFICATION)
            print(f'Subscribed to notifications for {uuid.toString()} on {self._sensor_address()}')
        print('emit do_authenticate')
        self.do_authenticate.emit()

    def _authenticate(self):
        pass

    def _is_connected(self) -> bool:
        print(f'is_connected {self._controller.state()} {self._controller and self._controller.state() == QLowEnergyController.ControllerState.DiscoveredState}')
        return self._controller and self._controller.state() == QLowEnergyController.ControllerState.DiscoveredState

    def __reset_connection(self) -> None:
        self.disconnected.emit('Disconnected')
        logging.debug(f"Disconnected from device, cleaning up")
        self.__remove_service()
        self.__remove_client()
        self._ble_device = None

    def __remove_service(self) -> None:
        if self._service is None:
            return
        try:
            logging.debug('Deleting bluetooth service')
            self._service.deleteLater()
        except Exception as e:
            logging.debug(f"Couldn't remove service: {e}")
        finally:
            self._service = None
            self._notifications = []

    def __remove_client(self) -> None:
        if self._controller is None:
            return
        try:
            logging.debug('Deleting bluetooth client')
            self._controller.disconnected.disconnect()
            self._controller.deleteLater()
        except Exception as e:
            print(f"Couldn't remove client: {e}")
        finally:
            self._controller = None

    def __catch_error(self, error) -> None:
        if error == QLowEnergyController.Error.ConnectionError:
            msg = f'Make sure the device is turned on and in range.'
        elif error == QLowEnergyController.Error.AuthorizationError:
            msg = f'The device is not authorized to connect to the device.'
        else:
            msg = f'An unknown error has occurred.'
        if self._controller is not None:
            msg = f'{self._controller.errorString()} {msg}'
        logging.debug(msg)
        self.error.emit(msg)
        self.__reset_connection()

    def _data_handler(self, char: QLowEnergyCharacteristic, data: QByteArray):
        pass

    def _write_characteristic(self, characteristic_uuid: QBluetoothUuid, data: bytearray) -> None:
        if self._service is None:
            self.error.emit('Service not initialized')
            return
        characteristic = self._service.characteristic(characteristic_uuid)
        if characteristic.isValid() and QLowEnergyCharacteristic.PropertyType.Write & characteristic.properties():
            # Write the characteristic
            logging.debug(f'Writing data: {BluetoothUtils.byte_array_to_hex_string(data)} to characteristic: {characteristic_uuid.toString()} {characteristic.properties}')
            print(f'Writing data: {BluetoothUtils.byte_array_to_hex_string(data)} to characteristic: {characteristic_uuid.toString()} {characteristic.properties}')
            self._service.writeCharacteristic(characteristic, data)
        else:
            self.error.emit(f'Characteristic: {characteristic_uuid.toString()} not found or not writable')

    def _set_next_expected_heartbeat(self):
        now = datetime.datetime.utcnow()
        self._next_heartbeat = now + datetime.timedelta(seconds=self._device_heartbeat_interval)
        logging.debug(f'Next heartbeat expected at {self._next_heartbeat} now: {now}')

    @property
    def _heartbeat_overdue(self):
        return datetime.datetime.utcnow() > self._next_heartbeat