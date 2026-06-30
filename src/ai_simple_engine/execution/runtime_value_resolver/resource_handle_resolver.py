from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.resources.handle.base import ResourceHandle


class ResourceHandleRuntimeValueResolver(
    RuntimeValueResolver
):
    """
    *BASIC ENGINE RUNTIME VALUE RESOLVER*

    Class to resolve and load the resources to
    be able to use them inside the operations.

    This `RuntimeValueResolver` will be added
    to the engine by default.
    """

    def is_supported(
        self,
        value: object
    ) -> bool:
        return isinstance(
            value,
            ResourceHandle
        )

    async def resolve(
        self,
        value: ResourceHandle,
        context: ExecutionContext
    ):
        """
        Resolve the `Resource` associated to the
        `ResourceHandle` instance given as `value`,
        by loading it to use it to perform the
        operations.
        """
        return context.resources.resolve(value).value