from ai_simple_engine.models.installed_model import InstalledModel
from abc import ABC, abstractmethod



class ModelLoader(
    ABC
):

    @property
    @abstractmethod
    def family(
        self
    ) -> str:
        ...

    @abstractmethod
    async def load(
        self,
        model: InstalledModel,
        *,
        device: str
    ) -> object:
        ...

    async def unload(
        self,
        instance: object
    ):
        pass