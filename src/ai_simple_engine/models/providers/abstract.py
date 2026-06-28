from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class ModelProvider(
    PluginComponent,
    ABC
):

    @property
    @abstractmethod
    def name(
        self
    ) -> str:
        ...

    @abstractmethod
    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...

    @abstractmethod
    def installed(
        self,
        spec: ModelSpec
    ) -> bool:
        ...

    @abstractmethod
    def get(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...