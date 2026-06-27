from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.types.data_type import DataType
from abc import abstractmethod


class DataTypeProvider(
    PluginProvider
):

    @abstractmethod
    def data_types(
        self
    ) -> list[DataType]:
        ...