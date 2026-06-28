from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.models.model_family import ModelFamily


class ModelLoaderRegistry:

    def __init__(
        self
    ):
        self._loaders: list[ModelLoader] = []

    def register(
        self,
        loader: ModelLoader
    ) -> None:
        self._loaders.append(loader)

    def get(
        self,
        family: ModelFamily
    ) -> ModelLoader:
        for loader in self._loaders:
            if loader.is_supported(family):
                return loader

        raise ValueError(f'The family "{family}" is not supported by these loaders.')