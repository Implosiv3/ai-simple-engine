from ai_simple_engine.execution.operation_runner.abstract import OperationRunner
from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.graph.operation.base import Operation


class LocalOperationRunner(
    OperationRunner
):

    async def run(
        self,
        operation: Operation,
        inputs: dict,
        context: ExecutionContext
    ) -> dict[str, object]:
        operation._begin_execution(inputs)

        try:
            return await operation.execute(context)

        finally:
            operation._end_execution()

        # return await operation.execute(context)