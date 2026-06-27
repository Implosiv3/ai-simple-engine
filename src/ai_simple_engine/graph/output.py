from ai_simple_engine.types.data_type import DataType
from ai_simple_engine.graph.port_reference import PortReference
from typing import Union


class Output:

    def __init__(
        self,
        type: DataType
    ):
        self.DataType = type
        self.name: Union[str, None] = None

    def __set_name__(
        self, 
        owner, 
        name
    ):
        self.name = name

    def __get__(
        self,
        instance,
        owner
    ):
        # From class
        if instance is None:
            return self

        # From an instance
        return PortReference(
            operation = instance,
            output = self
        )