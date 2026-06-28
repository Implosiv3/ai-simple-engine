from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.models.backends.abstract import ModelBackend
from abc import abstractmethod


class ModelRepositoryProvider(PluginProvider):

    @abstractmethod
    def model_providers(
        self
    ) -> list[ModelBackend]:
        ...