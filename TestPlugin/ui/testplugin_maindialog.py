from PyQt5.QtWidgets import QDialog
from qgis.gui import QgisInterface

from ..qgis_plugin_tools.tools.resources import load_ui

FORM_CLASS = load_ui("testplugin_base.ui")


class TestPluginMainDialog(QDialog, FORM_CLASS):

    def __init__(self, iface: QgisInterface, parent=None):
        """Constructor."""
        self.is_initializing = True

        # setup superclass
        super().__init__()

        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
