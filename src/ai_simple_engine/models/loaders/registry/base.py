from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.resolver_registry import ResolverRegistry


class ModelLoaderRegistry(
    ResolverRegistry[
        InstalledModel,
        ModelLoader,
        str
    ]
):

    def key_for(
        self,
        model: InstalledModel
    ) -> str:
        return model.family.name








# from ai_simple_engine.models.loaders.abstract import ModelLoader
# from ai_simple_engine.models.model_family import ModelFamily


# class ModelLoaderRegistry:

#     def __init__(
#         self
#     ):
#         self._loaders: list[ModelLoader] = []

#     def register(
#         self,
#         loader: ModelLoader
#     ) -> None:
#         self._loaders.append(loader)

#     def get(
#         self,
#         family: ModelFamily
#     ) -> ModelLoader:
#         for loader in self._loaders:
#             if loader.is_supported(family):
#                 return loader

#         raise ValueError(f'The family "{family}" is not supported by these loaders.')