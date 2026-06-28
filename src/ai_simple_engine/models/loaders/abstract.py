from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.plugins.plugin_component import PluginComponent
from ai_simple_engine.models.loaded_model import LoadedModel
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
        device: str
    ) -> LoadedModel:
        ...

    async def unload(
        self,
        instance: LoadedModel
    ):
        pass