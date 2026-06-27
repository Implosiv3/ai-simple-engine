from ai_simple_engine.execution.execution_context import ExecutionContext
from abc import ABC, abstractmethod


class RuntimeValueResolver(
    ABC
):

    @abstractmethod
    def is_supported(
        self,
        value: object
    ) -> bool:
        ...

    @abstractmethod
    def resolve(
        self,
        value: object,
        context: ExecutionContext
    ) -> object:
        ...