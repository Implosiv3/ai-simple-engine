from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.device.base import Device
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
            category = 'model',
            # identifier = self._model.id,
            # TODO: This is not a ModelSpec but an InstalledModel
            identifier = f'{self.model.provider}:{self.model.family}:{self.model.identifier}',
            device = str(self._device)
        )

    def __init__(
        self,
        model: InstalledModel,
        loader: ModelLoader,
        device: Device
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