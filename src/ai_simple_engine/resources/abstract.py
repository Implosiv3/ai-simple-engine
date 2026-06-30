from ai_simple_engine.resources.key.base import ResourceKey
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union


T = TypeVar('T')

class Resource(
    Generic[T],
    ABC
):
    """
    Base class for any reusable resource.
    """

    _instance: Union[T, None] = None

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

    
    async def load(
        self
    ):
        """
        Load the resource instance in memory if it is
        not already instantiated, using cache with the
        `._instance`.

        This method will return the instance of this
        `Resource`, that could be an instance of many
        differenet classes.
        """
        if not self._instance:
            self._instance = await self._load()

        return self._instance

    @abstractmethod
    async def _load(
        self
    ):
        """
        *For internal use only*

        Internal method to load the resource depending
        on its type.

        This method must be implemented by each resource.
        """
        ...

    async def unload(
        self
    ):
        """
        Unload the instance from memory, cleaning the
        internal `._instance` cache.
        """
        if self._instance:
            await self._unload()

    async def _unload(
        self
    ):
        """
        *For internal use only*

        Internal method to unload the resource depending
        on its type.

        This method must be implemented by each resource.
        """
        pass