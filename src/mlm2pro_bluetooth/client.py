from typing import Callable

from bleak import BleakClient, BLEDevice
from bleak.backends.service import BleakGATTService


class MLM2PROClient:

    def __init__(
        self,
        device: BLEDevice,
        connect_timeout: float = 10
    ) -> None:
        self.bleak_client = BleakClient(device, timeout=connect_timeout)
        self.connect_timeout = connect_timeout
        self.subscriptions = []
        self.started = False

    async def start(self) -> None:
        print('start')
        await self.connect()
        self.started = True

    async def stop(self) -> None:
        print('stop')
        if self.started:
            await self.disconnect()
        self.started = False

    async def connect(self) -> None:
        print('connect')
        if not self.is_connected:
            await self.bleak_client.connect()  # type: ignore
            #await self.bleak_client.pair()
            #self.__init_api()

    async def disconnect(self) -> None:
        print('disconnect')
        if self.is_connected:
            #await self.bleak_client.unpair()
            await self.bleak_client.disconnect()  # type: ignore

    @property
    def is_connected(self) -> bool:
        return self.bleak_client.is_connected

    async def supports_service(self, uuid) -> bool:
        return bool(await self.get_service(uuid))

    async def get_service(self, uuid) -> BleakGATTService:
        return self.bleak_client.services.get_service(uuid)

    async def write_characteristic(self, service: BleakGATTService,  data: bytearray, characteristic_uuid: str, response: bool = True) -> None:
        if service is None:
            raise Exception('Service not initialized')
        characteristic = service.get_characteristic(characteristic_uuid)
        print(f'characteristic: {characteristic} {characteristic.properties}')
        if characteristic is None or "write" not in characteristic.properties:
            raise Exception(f'Characteristic: {characteristic_uuid} not found or not writable')
        print('write auth')
        result = await self.bleak_client.write_gatt_char(characteristic.uuid, data, response)
        return result

    async def subscribe_to_characteristics(self, characteristics: list[str], notification_handler: Callable) -> None:
        print(f'subscribed: {self.subscriptions}')
        if len(self.subscriptions) <= 0:
            print('subscribing to characteristics')
            for characteristic in characteristics:
                print(f'subscribe to: {characteristic}')
                await self.bleak_client.start_notify(characteristic, notification_handler)
                self.subscriptions.append(characteristic)

    async def unsubscribe_to_characteristics(self):
        if len(self.subscriptions) > 0:
            print('unsubscribing to characteristics')
            for subscription in self.subscriptions:
                print(f'unsubscribe from: {subscription}')
                await self.bleak_client.stop_notify(subscription)
            self.subscriptions = []