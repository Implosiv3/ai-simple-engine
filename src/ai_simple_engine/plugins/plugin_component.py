from ai_simple_engine.plugins.plugin_context import PluginContext
from abc import ABC


class PluginComponent(
    ABC
):

    def configure(
        self,
        context: PluginContext
    ) -> None:
        """
        Called once when the Engine is built.
        """
        self._settings = context.settings