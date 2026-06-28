from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.plugins.plugin_component import PluginComponent
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.device.base import Device
from abc import ABC, abstractmethod


class ModelLoader(
    PluginComponent,
    ABC
):

    @abstractmethod
    def is_supported(
        self,
        family: str
    ) -> str:
        ...

    @abstractmethod
    async def load(
        self,
        model: InstalledModel,
        *,
        device: Device
    ) -> LoadedModel:
        ...

    async def unload(
        self,
        instance: LoadedModel
    ):
        pass