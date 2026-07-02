from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from uuid import uuid4
from abc import ABC


class Operation(
    ABC
):
    """
    *Abstract class*

    The base class for any kind of operation,
    that includes `inputs`, `outputs` and will
    perform some tasks in between.

    A task that must be performed. Examples:
    - Generate music
    - Generate image
    - Transcribe with Whisper

    It doesn't know how to download models, load
    them, execute transformers. It only defines
    the model that is needed and what should be
    done.
    """

    _inputs: dict[str, Input] = {}
    _outputs: dict[str, Output] = {}

    def __init__(
        self,
        **kwargs
    ):
        self.id = uuid4()
        self._connections: dict[str, object] = {}
        self._resolved_inputs: dict[str, object] = {}
        """
        *For internal use only*

        The value of the inputs that will be used
        when the operation is being executed. These
        are the real values and will be load by the
        executor just before performing the
        operation, and cleared when it is done.
        """
        
        unknown = set(kwargs) - self.inputs().keys()
        if unknown:
            raise TypeError(f'Unknown inputs: {", ".join(unknown)}')

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
        """
        *For internal use only*

        Set the `inputs` provided as the resolved
        inputs to be used in the operation.
        """
        self._resolved_inputs = inputs.copy()

    def _end_execution(
        self
    ) -> None:
        """
        *For internal use only*

        Clear the resolved inputs as the operation
        has finished.
        """
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
