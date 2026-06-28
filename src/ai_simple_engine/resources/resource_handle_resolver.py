from ai_simple_engine.execution.runtime_value_resolver import RuntimeValueResolver
from ai_simple_engine.resources.resource_handle import ResourceHandle


class ResourceHandleResolver(
    RuntimeValueResolver
):

    def is_supported(
        self,
        value
    ) -> bool:
        return isinstance(value, ResourceHandle)

    async def resolve(
        self,
        value: ResourceHandle,
        context
    ):
        return await context.resources.resolve(
            value
        )