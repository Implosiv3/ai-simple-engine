from ai_simple_engine.resources.resource_key import ResourceKey
from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')

class Resource(
    Generic[T],
    ABC
):
    """
    Base class for any reusable resource.
    """

    @property
    @abstractmethod
    def key(
        self
    ) -> ResourceKey:
        """
        Unique key that identifies this resource.

        Two Resources with the same key are considered
        the same resource and will share the loaded
        instance.
        """
        ...
    
    @abstractmethod
    async def load(
        self
    ):
        ...

    async def unload(
        self
    ):
        pass