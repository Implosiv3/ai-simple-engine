from ai_simple_engine.types.data_type import DataType
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.graph.port import Port


class Output(
    Port
):
    # def __init__(
    #     self,
    #     type: DataType
    # ):
    #     super().__init__(
    #         type = type,
    #         name = None
    #     )

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