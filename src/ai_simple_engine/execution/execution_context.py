from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.resources.manager.base import ResourceManager
from ai_simple_engine.models.repository.base import ModelRepository
from ai_simple_engine.models.loaders.registry.base import ModelLoaderRegistry
from ai_simple_engine.services.service_registry import ServiceRegistry
from ai_simple_engine.cache.base import Cache
from ai_simple_engine.settings.engine_settings import EngineSettings
from uuid import UUID


class ExecutionContext:
    """
    All the context that will be used when
    executing operations, providing the
    cache, services, settings, model
    loaders, etc.
    """

    def __init__(
        self,
        settings: EngineSettings,
        model_repository: ModelRepository,
        model_loader_registry: ModelLoaderRegistry,
        resource_manager: ResourceManager,
        cache: Cache,
        service_registry: ServiceRegistry
    ):
        self.settings: EngineSettings = settings
        """
        All the internal settings of the engine.
        """

        self.models = model_repository
        """
        Access to the model repository.
        """
        self.model_loaders = model_loader_registry
        self.resources = resource_manager
        self.cache = cache
        self.services = service_registry

        self._operation_outputs: dict[UUID, dict[str, object]] = {}

    def has_result(
        self,
        operation: Operation
    ) -> bool:
        return operation.id in self._operation_outputs

    def store(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ) -> None:
        self._operation_outputs[operation.id] = outputs

    def outputs(
        self,
        operation: Operation
    ) -> dict[str, object]:
        return self._operation_outputs[operation.id]

    def output(
        self,
        operation: Operation,
        name: str
    ) -> object:
        return self._operation_outputs[operation.id][name]