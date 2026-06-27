from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.graph.port_reference import PortReference
from uuid import uuid4
from abc import ABC, abstractmethod
from typing import Union


class Operation(
    ABC
):
    _inputs: dict[str, Input] = {}
    _outputs: dict[str, Output] = {}

    def __init__(
        self,
        **kwargs
    ):
        self.id = uuid4()
        self._connections: dict[str, object] = {}
        self._resolved_inputs: dict[str, object] = {}
        
        unknown = set(kwargs) - self.inputs().keys()
        if unknown:
            raise TypeError(f'Unknown inputs: {', '.join(unknown)}')

        for name, port in self.inputs().items():
            if name in kwargs:
                value = kwargs[name]
            elif port.has_default:
                value = port.default
            elif port.optional:
                value = None
            else:
                raise TypeError(f'Missing required input "{name}".')

            port.validate(value)

            self._connections[name] = value

    def __init_subclass__(
        cls,
    ):
        super().__init_subclass__()

        cls._inputs = {}
        cls._outputs = {}

        for value in vars(cls).values():
            if isinstance(value, Input):
                cls._inputs[value.name] = value
            elif isinstance(value, Output):
                cls._outputs[value.name] = value
            else:
                raise Exception('The operation parameter provided is not an "Input" nor "Output" instance.')

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

    def expand(
        self
    ) -> Union[PortReference, None]:
        """
        The ability to expand it into different
        operations. It doesn't exist if it is a
        simple operation.
        """
        return None

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
    
    @classmethod
    def schema(
        cls
    ) -> dict:
        return {
            'name': cls.__name__,
            'inputs': {
                name: port.schema()
                for name, port in cls.inputs().items()
            },
            'outputs': {
                name: port.schema()
                for name, port in cls.outputs().items()
            }
        }

    @abstractmethod
    async def execute(
        self,
        context
    ) -> dict[str, object]:
        ...

    