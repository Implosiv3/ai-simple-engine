from ai_simple_engine.graph.operation.base import Operation


class Graph:

    def __init__(
        self
    ):
        self._operations: list[Operation] = []

    @property
    def operations(
        self
    ) -> tuple[Operation, ...]:
        return tuple(self._operations)

    def add(
        self,
        operation: Operation
    ) -> Operation:
        if operation not in self._operations:
            self._operations.append(operation)

        return operation