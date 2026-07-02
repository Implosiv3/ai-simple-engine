from ai_simple_engine.cache.base import Cache
from ai_simple_engine.execution.executor import Executor
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.services.service_registry import ServiceRegistry
from ai_simple_engine.models.loaders.registry.base import ModelLoaderRegistry
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.resources.manager.base import ResourceManager
from ai_simple_engine.models.repository.base import ModelRepository
from ai_simple_engine.settings.engine_settings import EngineSettings
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
        settings: EngineSettings,
        graph_builder: GraphBuilder,
        executor: Executor,
        model_repository: ModelRepository,
        model_loader_registry: ModelLoaderRegistry,
        resource_manager: ResourceManager,
        cache: Cache,
        runtime_value_resolvers: Union[Iterable[RuntimeValueResolver], None] = None,
        services: ServiceRegistry,
    ):
        self._settings = settings
        self._graph_builder = graph_builder
        self._executor = executor

        self._model_repository = model_repository
        self._model_loader_registry = model_loader_registry
        self._resource_manager = resource_manager
        self._cache = cache
        self._runtime_value_resolvers = runtime_value_resolvers
        self._services = services

    async def run(
        self,
        *targets: PortReference
    ):
        context = ExecutionContext(
            settings = self._settings,
            model_repository = self._model_repository,
            model_loader_registry = self._model_loader_registry,
            resource_manager = self._resource_manager,
            cache = self._cache,
            service_registry = self._services,
        )

        await self._executor.run(
            targets = targets,
            context = context,
        )

        values = [
            context.output(
                target.operation,
                target.name,
            )
            for target in targets
        ]

        if len(values) == 1:
            return values[0]

        return tuple(values)

    def create_context(
        self
    ) -> ExecutionContext:
        return ExecutionContext(
            model_repository = self.model_repository,
            cache = self.cache,
            resource_manager = self.resource_manager
        )