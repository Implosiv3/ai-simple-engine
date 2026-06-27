from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.resources.resource_key import ResourceKey


class ModelResource(
    Resource
):
    
    @property
    def key(
        self
    ):
        return ResourceKey(
            type = 'model',
            identifier = self._model.id,
            device = self._device
        )

    def __init__(
        self,
        model: InstalledModel,
        loader: ModelLoader,
        device: str
    ):
        self._model = model
        self._loader = loader
        self._device = device

    async def load(
        self
    ):
        return await self._loader.load(
            self._model,
            device = self._device
        )
    
    async def unload(
        self,
        instance
    ):
        await self._loader.unload(instance)