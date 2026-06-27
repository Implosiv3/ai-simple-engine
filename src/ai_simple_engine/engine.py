from ai_simple_engine.cache.base import Cache
from ai_simple_engine.cache.memory_cache import MemoryCache
from ai_simple_engine.execution.executor import Executor
from ai_simple_engine.execution.operation_runner.abstract import OperationRunner
from ai_simple_engine.execution.operation_runner.local_operation_runner import LocalOperationRunner
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.execution.runtime_value_resolver.port_reference_resolver import PortReferenceRuntimeValueResolver
from ai_simple_engine.execution.runtime_value_resolver.resource_handle_resolver import ResourceHandleRuntimeValueResolver
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.models.model_repository import ModelRepository
from typing import Union, Iterable


class Engine:
    """
    The engine that has an specific configuration
    and is capable of perform the operations to
    obtain the final result.
    """

    def __init__(
        self,
        *,
        model_repository: Union[ModelRepository, None] = None,
        cache: Union[Cache, None] = None,
        resource_manager: Union[ResourceManager, None] = None,
        operation_runner: Union[OperationRunner, None] = None,
        runtime_value_resolvers: Union[Iterable[RuntimeValueResolver], None] = None,
    ):
        self.model_repository = (
            model_repository
            or
            # TODO: I don't have this one
            ModelRepository(
                providers = [
                    # HugginFaceModelProvider
                    # LocalModelProvider
                ]
            )
        )

        self.cache = (
            cache or
            # TODO: I don't have memory cache
            MemoryCache()
        )

        self.resource_manager = (
            resource_manager or
            ResourceManager()
        )

        self.operation_runner = (
            operation_runner or
            LocalOperationRunner()
        )

        self.runtime_value_resolvers = [
            PortReferenceRuntimeValueResolver(),
            ResourceHandleRuntimeValueResolver(),
        ]

        # TODO: Does this avoid repeated values (?)
        if runtime_value_resolvers:
            self.runtime_value_resolvers.extend(runtime_value_resolvers)

        self._graph_builder = GraphBuilder()

        self._executor = Executor(
            graph_builder = self._graph_builder,
            operation_runner = self.operation_runner,
            runtime_value_resolvers = self.runtime_value_resolvers,
        )

    async def execute(
        self,
        targets: Union[Operation, PortReference, Iterable[Operation, PortReference]]
    ):
        context = self.create_context()
        return await self._executor.run(targets, context)

    def create_context(
        self
    ) -> ExecutionContext:
        return ExecutionContext(
            model_repository = self.model_repository,
            cache = self.cache,
            resource_manager = self.resource_manager
        )