from ai_simple_engine.graph.graph_validator import GraphValidator
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.operation.fingerprint_builder import OperationFingerprintBuilder
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.exceptions.execution_error import ExecutionError
from ai_simple_engine.execution.execution_planner import ExecutionPlanner
from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.operation_runner.abstract import OperationRunner
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from collections.abc import Mapping, Sequence
from typing import Iterable, Union


class Executor:
    """
    The class that will process the operations
    in the order they have to be done.
    """

    def __init__(
        self,
        *,
        graph_builder: GraphBuilder,
        operation_runner: OperationRunner,
        runtime_value_resolvers: list[RuntimeValueResolver]
    ):
        self._graph_builder = graph_builder
        self._validator = GraphValidator()
        self._planner = ExecutionPlanner()
        self._operation_runner = operation_runner
        self._runtime_values_resolvers = runtime_value_resolvers

    async def run(
        self,
        targets: PortReference | Iterable[PortReference],
        context: ExecutionContext
    ) -> ExecutionContext:
        graph = self._graph_builder.build(targets)

        self._validator.validate(graph)

        plan = self._planner.build(graph)

        for node in plan.nodes:
            await self._execute(
                node.operation,
                context
            )

        return context
    
    async def _execute(
        self,
        operation: Operation,
        context: ExecutionContext
    ) -> None:
        fingerprint = OperationFingerprintBuilder.build(operation)

        if context.cache.contains(fingerprint):
            context.store(
                operation,
                context.cache.get(fingerprint)
            )

            return
        
        resolved_inputs = {}

        # TODO: Use 'Input' metadata (?)
        for input_name in operation.inputs():
            value = getattr(operation, input_name)

            resolved_inputs[input_name] = await self._resolve_value(
                value,
                context
            )
        
        operation._begin_execution(resolved_inputs)

        try:
            outputs = await self._operation_runner.run(
                operation = operation,
                inputs = resolved_inputs,
                context = context
            )
        finally:
            operation._end_execution()

        self._validate_outputs(
            operation,
            outputs
        )
        
        context.store(
            operation,
            outputs
        )

        context.cache.put(
            fingerprint,
            outputs
        )

    async def _resolve_value(
        self,
        value,
        context: ExecutionContext
    ):
        """
        This will allow us to resolve dynamically based
        on our resolvers, so we could add something in
        the future and we just need to add the resolver.
        """
        for resolver in self._runtime_values_resolvers:
            if resolver.is_supported(value):
                resolved = await resolver.resolve(
                    value,
                    context
                )

                # Maybe we need to resolve more
                return await self._resolve_value(
                    resolved,
                    context
                )
        
        if isinstance(value, Mapping):
            return {
                k: await self._resolve_value(v, context)
                for k, v in value.items()
            }
        
        # list, tuple, etc.
        if (
            isinstance(value, Sequence) and
            not isinstance(value, (str, bytes))
        ):
            return type(value)(
                await self._resolve_value(v, context)
                for v in value
            )

        return value

    def _validate_outputs(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ):
        expected = operation.outputs()

        for name, port in expected.items():
            if name not in outputs:
                raise ExecutionError(f'The output "{name}" was not an expected output.')

            value = outputs[name]

            try:
                port.type.validate(value)

            except TypeError as e:
                raise ExecutionError(f'Invalid value for output "{name}": {e}') from e
