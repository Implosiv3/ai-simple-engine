from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class ModelBackend(
    PluginComponent,
    ABC
):
    """
    Class to encapsulate the ability to obtain models
    from different sources, getting the specifications
    and returning an `InstalledModel` instance ready
    to use.
    """

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