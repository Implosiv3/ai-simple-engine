from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ai_simple_engine.graph.operation.base import Operation
    from ai_simple_engine.graph.output import Output


@dataclass(frozen = True, slots = True)
class PortReference:

    operation: Operation
    output: Output

    @property
    def name(
        self
    ) -> str:
        return self.output.name

    @property
    def type(
        self
    ):
        return self.output.type