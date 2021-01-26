from ..qgis_plugin_tools.tools.settings import get_setting, set_setting


def set_default_settings(force: bool = False):
    """Sets the default settings if not already set."""
    if not get_setting("log_level") or force:
        set_setting("log_level/stream", "DEBUG")
        set_setting("log_level/info", "DEBUG")
        set_setting("log_level/bar", "DEBUG")
