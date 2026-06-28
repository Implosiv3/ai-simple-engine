from ai_simple_engine.models.loaders.abstract import ModelLoader
from typing import Iterable


class ModelLoaderRegistry:

    def __init__(
        self,
        loaders: Iterable[ModelLoader]
    ):
        self._loaders = loaders

    def get(
        self,
        family: str
    ) -> ModelLoader:
        for loader in self._loaders:
            if loader.is_supported(family):
                return loader

        raise ValueError(f'The family "{family}" is not supported by these loaders.')