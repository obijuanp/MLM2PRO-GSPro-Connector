from pathlib import Path
from PySide6.QtCore import Signal
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from src.SettingsForm_ui import Ui_SettingsForm
from src.appdata import AppDataPaths
from src.devices import Devices
from src.settings import Settings, LaunchMonitor


class SettingsForm(QWidget, Ui_SettingsForm):

    saved = Signal()

    def __init__(self, settings: Settings, app_paths: AppDataPaths):
        super().__init__()
        self.app_paths = app_paths
        self.settings = settings
        self.setupUi(self)
        self.launch_monitor_combo.clear()
        self.launch_monitor_combo.addItems(SettingsForm.launchmonitor_as_list())
        self.close_button.clicked.connect(self.__close)
        self.save_button.clicked.connect(self.__save)
        self.file_browse_button.clicked.connect(self.__file_dialog)

    def showEvent(self, event: QShowEvent) -> None:
        self.devices = Devices(self.app_paths)
        self.default_device_combo.clear()
        self.default_device_combo.addItems(self.devices.as_list())
        self.__load_values()

    def __close(self):
        self.close()

    @staticmethod
    def launchmonitor_as_list():
        keys = []
        for key in LaunchMonitor.__dict__:
            if key != '__' not in key:
                keys.append(getattr(LaunchMonitor, key))
        return keys

    def __save(self):
        if self.__valid():
            self.settings.ip_address = self.ipaddress_edit.toPlainText()
            self.settings.port = int(self.port_edit.toPlainText())
            self.settings.gspro_path = self.gspro_path_edit.toPlainText()
            self.settings.grspo_window_name = self.gspro_window_name.toPlainText()
            self.settings.gspro_api_window_name = self.gspro_api_window_name.toPlainText()
            self.settings.device_id = self.launch_monitor_combo.currentText()
            self.settings.default_device = self.default_device_combo.currentText()
            self.settings.r10_connector_ip_address = self.r10_ip_edit.toPlainText()
            self.settings.r10_connector_port = int(self.r10_port_edit.toPlainText())
            self.settings.r10_connector_path = self.r10_path_edit.toPlainText()
            self.settings.save()
            self.saved.emit()
            QMessageBox.information(self, "Settings Updated", f"Settings have been updated.\nPlease exit and restart the Connector for the changes to take effect.")

    def __valid(self):
        error = True
        if len(self.ipaddress_edit.toPlainText()) <= 0:
            QMessageBox.information(self, "Error", "IP Address is required.")
            error = False
        if not error and len(self.port_edit.toPlainText()) <= 0:
            QMessageBox.information(self, "Error", "Port is required.")
            error = False
        if self.launch_monitor_combo.currentText() == LaunchMonitor.R10 and len(self.r10_ip_edit.toPlainText()) <= 0:
            QMessageBox.information(self, "Error", "R10 Connector IP Address is required.")
            error = False
        if self.launch_monitor_combo.currentText() == LaunchMonitor.R10 and len(self.r10_port_edit.toPlainText()) <= 0:
            QMessageBox.information(self, "Error", "R10 Connector Port is required.")
            error = False
        return error

    def __load_values(self):
        self.ipaddress_edit.setPlainText(self.settings.ip_address)
        self.port_edit.setPlainText(str(self.settings.port))
        self.gspro_path_edit.setPlainText(str(self.settings.gspro_path))
        self.gspro_window_name.setPlainText(str(self.settings.grspo_window_name))
        self.gspro_api_window_name.setPlainText(str(self.settings.gspro_api_window_name))
        self.launch_monitor_combo.setCurrentText(self.settings.device_id)
        device = 'None'
        if hasattr(self.settings, 'default_device') and self.settings.default_device != '':
            device = self.settings.default_device
        self.default_device_combo.setCurrentText(device)
        self.r10_ip_edit.setPlainText(self.settings.r10_connector_ip_address)
        self.r10_port_edit.setPlainText(str(self.settings.r10_connector_port))
        self.r10_path_edit.setPlainText(str(self.settings.r10_connector_path))


    def __file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            self.gspro_path_edit.toPlainText(),
            "Exe (*.exe *.lnk *.bat)"
        )
        if filename:
            path = Path(filename)
            self.gspro_path_edit.setPlainText(str(path))
