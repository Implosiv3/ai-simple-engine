from ai_simple_engine.graph.graph_validator import GraphValidator
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.operation.fingerprint_builder import FingerprintBuilder
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
    *Do not instantiate this class, use `.execute`
    instead*
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
        outputs: PortReference | Iterable[PortReference],
        context: ExecutionContext
    ) -> ExecutionContext:
        graph = self._graph_builder.build(outputs)

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
        fingerprint = FingerprintBuilder.build(operation)

        if context.cache.contains(fingerprint):
            context.store(
                operation,
                context.cache.get(fingerprint)
            )

            return
        
        resolved_inputs = {
            name: self._resolve_value(value, context)
            for name, value in operation._connections.items()
        }
        
        operation._begin_execution(resolved_inputs)

        try:
            outputs = await self._operation_runner.run(
                operation,
                context
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

    def _resolve_parameters(
        self,
        operation: Operation,
        context: ExecutionContext
    ) -> dict[str, object]:
        parameters = {}

        for field in operation.model_fields:
            value = getattr(operation, field)

            parameters[field] = self._resolve_value(
                value,
                context
            )

        return parameters
    
    def _resolve_value(
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
                resolved = resolver.resolve(
                    value,
                    context
                )

                # Maybe we need to resolve more
                return self._resolve_value(
                    resolved,
                    context
                )
        
        if isinstance(value, Mapping):
            return {
                k: self._resolve_value(v, context)
                for k, v in value.items()
            }
        
        # list, tuple, etc.
        if (
            isinstance(value, Sequence) and
            not isinstance(value, (str, bytes))
        ):
            return type(value)(
                self._resolve_value(v, context)
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

            if (
                port.type.runtime_type is not object and
                not isinstance(value, port.type.runtime_type)
            ):
                # TODO: Maybe say what was expected (?)
                raise ExecutionError(f'The output "{name}" type is not the expected one.')
    

async def execute(
    targets: Union[Operation, PortReference, Iterable[Union[Operation, PortReference]]]
):
    executor = Executor()

    context = await executor.run(targets)

    if isinstance(targets, Operation):
        return None

    if isinstance(targets, PortReference):
        return context.output(
            targets.operation,
            targets.name
        )

    results = []

    for target in targets:
        if isinstance(target, Operation):
            results.append(None)
        else:
            results.append(
                context.output(
                    target.operation,
                    target.name
                )
            )

    return results