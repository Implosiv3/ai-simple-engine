from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.models.loaders.abstract import ModelLoader
from abc import abstractmethod


class ModelLoaderProvider(
    PluginProvider
):

    @abstractmethod
    def model_loaders(
        self
    ) -> list[ModelLoader]:
        ...