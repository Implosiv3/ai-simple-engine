from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.graph.operation.base import Operation
from abc import abstractmethod


class OperationProvider(
    PluginProvider
):

    @abstractmethod
    def operations(
        self
    ) -> list[type[Operation]]:
        ...