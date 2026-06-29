from ai_simple_engine.plugins.plugin import Plugin
from ai_simple_engine.engine import Engine
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.cache.memory_cache import MemoryCache
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.models.backends.model_backend_registry import ModelBackendRegistry
from ai_simple_engine.execution.operation_runner.local_operation_runner import LocalOperationRunner
from ai_simple_engine.execution.operation_runner.abstract import OperationRunner
from ai_simple_engine.execution.executor import Executor
from ai_simple_engine.models.model_repository import ModelRepository
from ai_simple_engine.models.loaders.model_loader_registry import ModelLoaderRegistry
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.execution.runtime_value_resolver.resource_handle_resolver import ResourceHandleRuntimeValueResolver
from ai_simple_engine.execution.runtime_value_resolver.port_reference_resolver import PortReferenceRuntimeValueResolver
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.types.data_type import DataType
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.types.validator.abstract import DataTypeValidator
from ai_simple_engine.settings.engine_settings import EngineSettings
from ai_simple_engine.plugins.plugin_context import PluginContext
from ai_simple_engine.services.service_registry import ServiceRegistry, T


class EngineBuilder:

    def __init__(
        self
    ):
        self._settings = EngineSettings()
        self._services = ServiceRegistry()
        self._operation_runner = LocalOperationRunner()
        self._graph_builder = GraphBuilder()
        self._cache = MemoryCache()
        self._resource_manager = ResourceManager()

        self._model_loaders = []
        self._model_backends = []
        self._runtime_value_resolvers = [
            PortReferenceRuntimeValueResolver(),
            ResourceHandleRuntimeValueResolver()
        ]
        self._operations = []
        self._data_types = []
        # TODO: What about the validators (?)
        self._data_type_validators = []

        self._instantiate_executor()

        self._was_built:bool = False
        """
        Internal boolean flag to control when the
        builder has already built an engine.
        """

    def _instantiate_executor(
        self
    ) -> 'EngineBuilder':
        """
        *For internal use only*

        Create (or recreate if existing) the executor
        instance:

        ```
        self._executor = Executor(
            graph_builder = self._graph_builder,
            operation_runner = self._operation_runner,
            runtime_value_resolvers = self._runtime_value_resolvers
        )
        ```
        """
        self._executor = Executor(
            graph_builder = self._graph_builder,
            operation_runner = self._operation_runner,
            runtime_value_resolvers = self._runtime_value_resolvers
        )

        return self

    def set_operation_runner(
        self,
        operation_runner: OperationRunner
    ) -> 'EngineBuilder':
        self._operation_runner = operation_runner

        self._instantiate_executor()

        return self

    def add_model_loader(
        self,
        loader: ModelLoader
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repeated ones (?)
        self._model_loaders.append(loader)

        return self
    
    def add_operation(
        self,
        operation: Operation
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repeated ones (?)
        self._operations.append(operation)

        return self
    
    def add_data_type(
        self,
        data_type: DataType
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repeated ones (?)
        self._data_types.append(data_type)

        return self
    
    def add_runtime_value_resolver(
        self,
        runtime_value_resolver: RuntimeValueResolver
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repeated ones (?)
        self._runtime_value_resolvers.append(runtime_value_resolver)

        return self
    
    def add_model_backend(
        self,
        model_backend: ModelBackend
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repeated ones (?)
        self._model_backends.append(model_backend)

        return self
    
    def add_data_type_validator(
        self,
        validator: DataTypeValidator
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        # TODO: What about repated ones (?)
        self._data_type_validators.append(validator)

        return self
    
    def add_plugin(
        self,
        plugin: Plugin
    ) -> 'EngineBuilder':
        self._ensure_not_built()

        plugin.register(self)

        return self

    def add_service(
        self,
        service_type: type[T],
        service: T
    ) -> 'EngineBuilder':
        """
        The `service_type` is to identify it in a unique
        way so we can get it later, but letting us to
        obtain a custom class if we want to. Here you
        have one example:

        ```
        class HttpClient(ABC):
            ...

        class RequestsHttpClient(HttpClient):
            ...

        builder.add_service(
            HttpClient,
            RequestsHttpClient()
        )
        ```
        """
        self._ensure_not_built()

        self._services.register(
            service_type,
            service
        )

        return self

    def build(
        self
    ) -> Engine:
        self._ensure_not_built()

        backend_registry = self._build_model_backend_registry()
        model_loader_registry = self._build_model_loader_registry()

        self._services.register(
            ModelBackendRegistry,
            backend_registry
        )

        self._services.register(
            ModelLoaderRegistry,
            model_loader_registry
        )

        plugin_context = PluginContext(
            settings = self._settings,
            services = self._services
        )

        self._configure_components(plugin_context)

        model_repository = ModelRepository(
            backend_registry
        )

        self._was_built = True

        return Engine(
            settings = self._settings,
            graph_builder = self._graph_builder,
            executor = self._executor,
            model_repository = model_repository,
            model_loader_registry = model_loader_registry,
            resource_manager = self._resource_manager,
            cache = self._cache,
            runtime_value_resolvers = self._runtime_value_resolvers,
            services = self._services,
        )
    
    def _configure_components(
        self,
        plugin_context: PluginContext
    ) -> None:
        """
        *For internal use only*
        """
        components = [
            *self._model_backends,
            *self._model_loaders,
            *self._runtime_value_resolvers,
            *self._data_type_validators,
        ]

        for component in components:
            component.configure(plugin_context)
    
    def _build_model_backend_registry(
        self
    ) -> ModelBackendRegistry:
        """
        *For internal use only*
        """
        registry = ModelBackendRegistry()

        for backend in self._model_backends:
            registry.register(
                backend.provider,
                backend
            )

        return registry
    
    def _build_model_loader_registry(
        self
    ) -> ModelLoaderRegistry:
        """
        *For internal use only*
        """
        model_loader_registry = ModelLoaderRegistry()

        for model_loader in self._model_loaders:
            model_loader_registry.register(
                model_loader.family,
                model_loader
            )

        return model_loader_registry

    def _ensure_not_built(
        self
    ) -> None:
        if self._was_built:
            raise RuntimeError('This EngineBuilder has already been used to build an Engine.')
        
    