"""bd_schema_plugin Plugin Initilization."""

from nautobot.extras.plugins import PluginConfig


class BdSchemaPluginConfig(PluginConfig):
    """Plugin configuration for the bd_schema_plugin plugin."""

    name = "bd_schema_plugin"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "bd_schema_plugin"  # Human-friendly name for the plugin.
    base_url = "bd_schema_plugin"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "2.1.1"  # Maximum version of Nautobot with which the plugin is compatible.
    default_settings = {}  # A dictionary of configuration parameters and their default values.


config = BdSchemaPluginConfig
