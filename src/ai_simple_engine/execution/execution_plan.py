from ai_simple_engine.execution.execution_node import ExecutionNode


class ExecutionPlan:

    def __init__(
        self,
        nodes: list[ExecutionNode]
    ):
        self._nodes = tuple(nodes)

    @property
    def nodes(
        self
    ):
        return self._nodes