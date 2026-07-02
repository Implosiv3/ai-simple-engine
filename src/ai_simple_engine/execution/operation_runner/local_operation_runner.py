from ai_simple_engine.execution.operation_runner.abstract import OperationRunner
from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.graph.operation.abstract.base import Operation


class LocalOperationRunner(
    OperationRunner
):

    async def run(
        self,
        operation: Operation,
        # Let it here to respect the structure
        inputs: dict,
        context: ExecutionContext
    ) -> dict[str, object]:
        return await operation.execute(context)