from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.spec.base import ModelSpec
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class ModelBackend(
    PluginComponent,
    ABC
):
    """
    Class to obtain models with the given `ModelSpec`
    from different sources (providers) and install them
    as `InstalledModel` to be able to use them later.
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