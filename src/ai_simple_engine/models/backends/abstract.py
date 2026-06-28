from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class ModelBackend(
    PluginComponent,
    ABC
):

    @property
    @abstractmethod
    def name(
        self
    ) -> str:
        ...

    @property
    @abstractmethod
    def provider(
        self
    ) -> str:
        """
        Unique provider identifier (e.g. 'huggingface',
        'local', 's3').
        """
        ...

    @abstractmethod
    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...

    @abstractmethod
    def is_installed(
        self,
        spec: ModelSpec
    ) -> bool:
        ...

    @abstractmethod
    def get_installed_model(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...