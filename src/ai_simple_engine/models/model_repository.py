from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.models.backends.model_backend_registry import ModelBackendRegistry
from ai_simple_engine.models.model_spec import ModelSpec
# from ai_simple_engine.settings.engine_settings import EngineSettings
# from typing import Iterable


class ModelRepository:
    
    def __init__(
        self,
        backends: ModelBackendRegistry,
        # providers: Iterable[ModelBackend],
        # settings: EngineSettings
    ):
        self._backends = backends

        # self._providers = {
        #     provider.name: provider
        #     for provider in providers
        # }

        # self._settings: EngineSettings = settings

    def _provider(
        self,
        spec: ModelSpec
    ) -> ModelBackend:
        try:
            return  self._backends.resolve(spec)

        except KeyError:
            raise ValueError(f'Unknown model backend "{spec.provider}".')

        try:
            return self._providers[spec.provider]

        except KeyError:
            raise ValueError(f'Unknown model provider "{spec.provider}".')
        
    # def configure(
    #     self,
    #     settings: EngineSettings
    # ) -> None:
    #     self._settings = settings

    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        """
        Install the model with the given `spec` and
        return it as an `InstalledModel` instance.
        """
        backend = self._backends.resolve(spec)

        return await backend.install(spec)

    def is_installed(
        self,
        spec: ModelSpec
    ) -> bool:
        """
        Check if the model with the given `spec` is
        installed or not.
        """
        backend = self._backends.resolve(spec)

        return backend.is_installed(spec)

    def get_installed_model(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        """
        Get the model with the given `spec` as an
        `InstalledModel` instance.
        """
        backend = self._backends.resolve(spec)

        return backend.get_installed_model(spec)