from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.plugins.plugin_component import PluginComponent
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.device.base import Device
from abc import ABC, abstractmethod


class ModelLoader(
    PluginComponent,
    ABC
):
    """
    Class to load a model and make it ready to use.
    This will transform an `InstalledModel` into a
    `LoadedModel` that can be used in the way it
    should be; I mean, the implementation will be
    specifically made for that model, which could
    be using transformers, torch, diffusers, etc.
    """
    
    @property
    @abstractmethod
    def family(
        self
    ) -> str:
        ...

    def is_supported(
        self,
        family: str
    ) -> str:
        return self.family == family

    @abstractmethod
    async def load(
        self,
        installed_model: InstalledModel,
        device: Device
    ) -> object:
        ...

    async def unload(
        self,
        instance: LoadedModel
    ):
        pass