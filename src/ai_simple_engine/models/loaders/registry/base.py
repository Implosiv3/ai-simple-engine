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
        return model.family