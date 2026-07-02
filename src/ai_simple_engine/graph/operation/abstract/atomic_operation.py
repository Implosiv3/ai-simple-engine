from ai_simple_engine.graph.operation.abstract.base import Operation
from abc import ABC, abstractmethod


class AtomicOperation(
    Operation,
    ABC
):
    
    @abstractmethod
    async def execute(
        self,
        context: 'ExecutionContext'
    ) -> dict[str, object]:
        """
        The code that will perform the real operation
        with the values that have being resolved in
        the `_begin_execution` method and are restored
        in the `_end_execution` method.

        This method will be called by the executor in
        between the call to those 2 methods.
        """
        ...