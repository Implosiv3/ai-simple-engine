from ai_simple_engine.resources.abstract import Resource
from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.device.base import Device
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.resources.key.base import ResourceKey


class ModelResource(
    Resource[LoadedModel]
):
    """
    A model resource that is capable of loading
    a model by using its specific loader.
    """
    
    @property
    def key(
        self
    ):
        return ResourceKey(
            category = 'model',
            identifier = f'{self._model.provider}:{self._model.family}:{self._model.identifier}',
            variant = str(self._device)
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

    async def _load(
        self
    ) -> LoadedModel:
        """
        *For internal use only*

        Load the model resource by using the loader
        provided.
        """
        return await self._loader.load(
            self._model,
            device = self._device
        )
    
    async def unload(
        self,
        instance
    ) -> None:
        await self._loader.unload(instance)