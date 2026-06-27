from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.resources.resource_handle import ResourceHandle


class ResourceHandleRuntimeValueResolver(
    RuntimeValueResolver
):

    def is_supported(
        self,
        value: object
    ) -> bool:
        return isinstance(
            value,
            ResourceHandle
        )

    def resolve(
        self,
        value: ResourceHandle,
        context: ExecutionContext
    ):
        return context.resources.get(value)