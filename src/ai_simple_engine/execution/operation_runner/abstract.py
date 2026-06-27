from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.graph.operation.base import Operation
from abc import ABC, abstractmethod


class OperationRunner(
    ABC
):

    @abstractmethod
    async def run(
        self,
        operation: Operation,
        context: ExecutionContext
    ) -> dict[str, object]:
        ...