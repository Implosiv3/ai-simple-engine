from abc import ABC, abstractmethod


class Resource(
    ABC
):
    """
    Base class for any reusable resource.
    """
    
    @abstractmethod
    async def load(
        self
    ):
        ...

    async def unload(
        self
    ):
        pass