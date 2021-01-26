from types import SimpleNamespace
from typing import List, Union

from qgis.core import QgsVectorLayer, QgsRasterLayer, QgsProject

from ..definitions.file_extensions import VECTOR_EXTENSIONS, RASTER_EXTENSIONS
from ..ui.testplugin_maindialog import TestPluginMainDialog


class LayerLoader:

    def __init__(self, ui: TestPluginMainDialog):
        """Sets up the LayerLoader."""
        self.ui = ui

    def load_layers(self):
        """Loads the layers based on ui settings."""
        settings = self.ui.get_user_input()
        file_suffix = settings.filepath.suffix

        if file_suffix in VECTOR_EXTENSIONS:
            layer_class = QgsVectorLayer
        elif file_suffix in RASTER_EXTENSIONS:
            layer_class = QgsRasterLayer
        else:
            raise Exception("Invalid file extension")

        layers = self.__create_layers(layer_class, settings)
        # noinspection PyArgumentList
        QgsProject.instance().addMapLayers(layers)

    @staticmethod
    def __create_layers(layer_class: Union[type(QgsVectorLayer), type(QgsRasterLayer)],
                        settings: SimpleNamespace) -> List[Union[QgsVectorLayer, QgsRasterLayer]]:
        """Creates and returns a list of layers."""
        layers = []
        base_name = settings.filepath.stem
        for i in range(settings.copies):
            layers.append(layer_class(str(settings.filepath), f"{base_name}_{i+1}"))

        return layers
