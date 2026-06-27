from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.graph.port_reference import PortReference
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr
from abc import ABC, abstractmethod
from typing import Union


class Operation(
    BaseModel,
    ABC
):
    model_config = ConfigDict(
        arbitrary_types_allowed = True,
        extra = 'forbid'
    )

    id: UUID = Field(
        default_factory = uuid4,
        frozen = True
    )

    _inputs: dict[str, Input] = {}
    _outputs: dict[str, Output] = {}
    _graph = PrivateAttr(default=None)
    """
    Non-serialized internal execution data.
    """

    _connections: dict[str, Union[PortReference, object]] = PrivateAttr(default_factory=dict)

    def __init__(
        self,
        **data
    ):
        inputs = {}

        for name in self.inputs():
            if name in data:
                inputs[name] = data.pop(name)

        super().__init__(**data)

        self._connections = inputs

    def __init_subclass__(
        cls, 
        **kwargs
    ):
        super().__init_subclass__(**kwargs)

        cls._inputs = {}
        cls._outputs = {}

        for name, value in vars(cls).items():
            if isinstance(value, Input):
                cls._inputs[name] = value
            elif isinstance(value, Output):
                cls._outputs[name] = value
            else:
                raise Exception('The operation parameter provided is not expected.')

    def __hash__(
        self
    ) -> int:
        return hash(self.id)

    def __eq__(
        self,
        other
    ) -> bool:
        return (
            isinstance(other, Operation)
            and self.id == other.id
        )
    
    def _begin_execution(
        self,
        inputs: dict[str, object]
    ) -> None:
        self._resolved_inputs = inputs

    def _end_execution(
        self
    ) -> None:
        self._resolved_inputs.clear()

    @classmethod
    def inputs(
        cls
    ) -> dict[str, Input]:
        return cls._inputs

    @classmethod
    def outputs(
        cls
    ) -> dict[str, Output]:
        return cls._outputs

    @abstractmethod
    async def execute(
        self,
        context
    ) -> dict[str, object]:
        ...