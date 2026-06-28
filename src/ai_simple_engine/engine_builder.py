from ai_simple_engine.plugins.plugin import Plugin
from ai_simple_engine.plugins.plugin_registry import PluginRegistry
from ai_simple_engine.engine import Engine
from ai_simple_engine.graph.graph_builder import GraphBuilder
from ai_simple_engine.cache.memory_cache import MemoryCache
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.models.backends.model_backend_registry import ModelBackendRegistry
from ai_simple_engine.execution.operation_runner.local_operation_runner import LocalOperationRunner
from ai_simple_engine.models.model_repository import ModelRepository
from ai_simple_engine.models.loaders.model_loader_registry import ModelLoaderRegistry
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.plugins.providers.operation_provider import OperationProvider
from ai_simple_engine.plugins.providers.model_loader_provider import ModelLoaderProvider
from ai_simple_engine.plugins.providers.model_repository_provider import ModelRepositoryProvider
from ai_simple_engine.plugins.providers.runtime_value_resolver_provider import RuntimeValueResolverProvider
from ai_simple_engine.plugins.providers.data_type_provider import DataTypeProvider
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

        self._graph_builder = GraphBuilder()
        self._cache = MemoryCache()
        self._resource_manager = ResourceManager()
        self._operation_runner = LocalOperationRunner()

        self._model_loaders = []
        self._model_backends = []
        self._runtime_value_resolvers = []
        self._operations = []
        self._data_types = []
        # TODO: What about the validators (?)
        self._data_type_validators = []

        self._was_built:bool = False
        """
        Internal boolean flag to control when the
        builder has already built an engine.
        """

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
    ):
        self._ensure_not_built()

        for provider in plugin.providers():
            self.add_provider(provider)

    def add_provider(
        self,
        provider: PluginProvider
    ):
        self._ensure_not_built()

        # The provider is now active
        provider.register(self)

        # if isinstance(provider, ModelLoaderProvider):
        #     self._model_loaders.extend(
        #         provider.model_loaders()
        #     )

        # if isinstance(provider, ModelRepositoryProvider):
        #     self._model_backends.extend(
        #         provider.model_providers()
        #     )

        # if isinstance(provider, RuntimeValueResolverProvider):
        #     self._runtime_value_resolvers.extend(
        #         provider.runtime_value_resolvers()
        #     )

        # if isinstance(provider, DataTypeProvider):
        #     self._data_types.extend(
        #         provider.data_types()
        #     )

        # if isinstance(provider, OperationProvider):
        #     self._operations.extend(
        #         provider.operations()
        #     )

        # TODO: What about the validators (?)

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

        plugin_context = PluginContext(
            settings = self._settings,
            services = self._services
        )



        registry = ModelBackendRegistry()

        for backend in self._model_backends:
            registry.register(
                backend.provider,
                backend
            )

        model_repository = ModelRepository(
            registry
        )




        model_loader_registry = ModelLoaderRegistry()

        for model_loader in self._model_loaders:
            model_loader_registry.register(model_loader)

        # Set the plugin context
        for provider in self._model_backends:
            provider.configure(plugin_context)

        # for model_loader in self._model_loaders:
        #     model_loader.configure(plugin_context)

        for runtime_value_resolver in self._runtime_value_resolvers:
            runtime_value_resolver.configure(plugin_context)

        self._was_built = True

        return Engine(
            settings = self._settings,
            model_repository = model_repository,
            cache = self._cache,
            resource_manager = self._resource_manager,
            operation_runner = self._operation_runner,
            runtime_value_resolvers = self._runtime_value_resolvers,

            graph_builder = self._graph_builder,
            model_loader_registry = model_loader_registry
        )

    def _ensure_not_built(
        self
    ) -> None:
        if self._was_built:
            raise RuntimeError('This EngineBuilder has already been used to build an Engine.')
        
    