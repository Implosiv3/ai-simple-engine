from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.graph.port_reference import PortReference


class PortReferenceRuntimeValueResolver(
    RuntimeValueResolver
):

    def is_supported(
        self,
        value: object
    ) -> bool:
        return isinstance(
            value,
            PortReference
        )

    async def resolve(
        self,
        value: PortReference,
        context: ExecutionContext
    ):
        return await context.output(
            value.operation,
            value.name
        )