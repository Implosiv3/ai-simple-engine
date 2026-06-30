from ai_simple_engine.plugins.plugin import Plugin
from collections.abc import Iterable


class PluginRegistry:
    """
    Registry in which we include all the plugins
    that we are including.
    """

    def __init__(
        self
    ):
        self._plugins: list[Plugin] = []

    def register(
        self,
        plugin: Plugin
    ) -> None:
        self._plugins.append(plugin)

    def plugins(
        self
    ) -> Iterable[Plugin]:
        return tuple(self._plugins)