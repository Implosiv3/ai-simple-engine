from ai_simple_engine.graph.operation.base import Operation
from dataclasses import dataclass, field


@dataclass(slots = True, eq = False)
class ExecutionNode:

    operation: Operation
    dependencies: list['ExecutionNode'] = field(default_factory = list)
    dependents: list['ExecutionNode'] = field(default_factory = list)