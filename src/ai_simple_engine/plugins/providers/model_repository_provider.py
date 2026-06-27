from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.models.providers.abstract import ModelProvider
from abc import abstractmethod


class ModelRepositoryProvider(PluginProvider):

    @abstractmethod
    def model_providers(
        self
    ) -> list[ModelProvider]:
        ...