from ai_simple_engine.plugins.plugin_context import PluginContext
from abc import ABC


class PluginComponent(
    ABC
):
    """
    *Abstract class*

    Class to be inherited by any other class
    that is a component of a plugin and has to
    be configured with an specific
    `PluginContext`.
    """

    def configure(
        self,
        context: PluginContext
    ) -> None:
        """
        Called once when the Engine is built just to
        set the context settings.
        """
        self._settings = context.settings