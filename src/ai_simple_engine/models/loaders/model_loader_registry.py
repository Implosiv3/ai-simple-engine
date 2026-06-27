from ai_simple_engine.models.loaders.abstract import ModelLoader
from typing import Iterable


class ModelLoaderRegistry:

    def __init__(
        self,
        loaders: Iterable[ModelLoader]
    ):
        self._loaders = {
            loader.family: loader
            for loader in loaders
        }

    def get(
        self,
        family: str
    ) -> ModelLoader:
        return self._loaders[family]