from ai_simple_engine.types.data_type import DataType
from typing import Union


class Input:

    def __init__(
        self,
        type: DataType,
        optional: bool = False
    ):
        self.type = type
        self.optional = optional
        self.name: Union[str, None] = None

    def __get__(
        self,
        instance,
        owner
    ):
        if instance is None:
            return self

        if self.name in instance._resolved_inputs:
            return instance._resolved_inputs[self.name]

        return instance._connections[self.name]

    def __set_name__(
        self,
        owner,
        name
    ):
        self.name = name