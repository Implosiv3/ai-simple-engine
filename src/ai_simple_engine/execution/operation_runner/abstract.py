from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.graph.operation.abstract.base import Operation
from abc import ABC, abstractmethod


class OperationRunner(
    ABC
):

    @abstractmethod
    async def run(
        self,
        operation: Operation,
        inputs: dict,
        context: ExecutionContext
    ) -> dict[str, object]:
        """
        This method will run the `operation` with the
        given `context`. The `inputs` could be necessary
        in some cases (serialization for an external
        service), so it must be implemented by all the
        `OperationRunner` classes.
        """
        ...