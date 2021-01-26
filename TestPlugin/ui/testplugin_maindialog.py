from pathlib import Path
from types import SimpleNamespace

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from qgis.gui import QgisInterface

from ..qgis_plugin_tools.tools.resources import load_ui

FORM_CLASS = load_ui("testplugin_base.ui")


class TestPluginMainDialog(QDialog, FORM_CLASS):

    def __init__(self, iface: QgisInterface, parent=None):
        """Constructor."""
        self.is_initializing = True

        # setup superclass
        # noinspection PyArgumentList
        super().__init__()

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface

        self.reset_ui()
        self.__setup_connections()
        self.is_initializing = False

    def reset_ui(self):
        """Sets UI to default state"""
        # Set filepath to nothing
        self.filewidget_input.setFilePath("")

        # Set copies to 1
        self.spinbox_copies.setClearValue(1)
        self.spinbox_copies.clear()

    def __setup_connections(self):
        """Sets up connections from signals to slots."""
        self.filewidget_input.fileChanged.connect(self.__on_filepath_changed)

    @pyqtSlot()
    def __on_filepath_changed(self):
        """Validate input filepath on fileChanged signal."""
        file_path = Path(self.filewidget_input.filePath())
        if not file_path.exists():
            raise Exception("File path does not exist")
        print("File does exist")

    def get_user_input(self) -> SimpleNamespace:
        """Reads user input from ui and returns a settings SimpleNamespace"""
        return SimpleNamespace(
            filepath=Path(self.filewidget_input.filePath()),
            copies=self.spinbox_copies.value(),
        )
