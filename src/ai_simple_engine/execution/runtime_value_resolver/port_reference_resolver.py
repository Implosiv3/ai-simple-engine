from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.graph.port_reference import PortReference


class PortReferenceRuntimeValueResolver(
    RuntimeValueResolver
):
    """
    *BASIC ENGINE RUNTIME VALUE RESOLVER*

    Class to resolve the `PortReference`
    instances (inputs, outputs) to be able to
    use them.

    This `RuntimeValueResolver` will be added
    to the engine by default.
    """

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
        return context.output(
            value.operation,
            value.name
        )