from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.providers.abstract import ModelProvider
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.settings.engine_settings import EngineSettings
from typing import Iterable


class ModelRepository:
    
    def __init__(
        self,
        providers: Iterable[ModelProvider],
        settings: EngineSettings
    ):
        self._providers = {
            provider.name: provider
            for provider in providers
        }

        self._settings: EngineSettings = settings

    def _provider(
        self,
        spec: ModelSpec
    ) -> ModelProvider:
        try:
            return self._providers[spec.provider]

        except KeyError:
            raise ValueError(f'Unknown model provider "{spec.provider}".')
        
    def configure(
        self,
        settings: EngineSettings
    ) -> None:
        self._settings = settings

    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        """
        Install the model with the given `spec` and
        return it as an `InstalledModel` instance.
        """
        return await self._provider(spec).install(spec)

    def is_installed(
        self,
        spec: ModelSpec
    ) -> bool:
        """
        Check if the model with the given `spec` is
        installed or not.
        """
        return self._provider(spec).is_installed(spec)

    def get_installed_model(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        """
        Get the model with the given `spec` as an
        `InstalledModel` instance.
        """
        return self._provider(spec).get_installed_model(spec)