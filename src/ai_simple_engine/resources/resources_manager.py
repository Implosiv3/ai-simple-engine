from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.resources.resource_handle import ResourceHandle
from ai_simple_engine.resources.loaded_resource import LoadedResource
from typing import Union


class ResourceManager:

    def __init__(
        self
    ):
        self._resources: dict[str, LoadedResource] = {}

    async def load(
        self,
        resource: Resource
    ) -> ResourceHandle:
        loaded = self._resources.get(resource.key)

        if loaded is not None:
            loaded.references += 1

            return ResourceHandle(resource.key)

        instance = await resource.load()

        self._resources[resource.key] = LoadedResource(
            resource = resource,
            instance = instance
        )

        return ResourceHandle(resource.key)
    
    def get(
        self,
        handle: ResourceHandle
    ) -> Resource:
        return self._resources[handle.key]
    
    async def unload(
        self,
        handle: ResourceHandle
    ):
        loaded = self._resources.get(handle.key)

        if loaded is None:
            return

        loaded.references -= 1

        if loaded.references > 0:
            return

        await loaded.resource.unload(
            loaded.instance
        )

        del self._resources[
            handle.key
        ]

    """
    TODO: I don't know if we really need these
    methods below.
    """
    # async def register(
    #     self,
    #     handle: ResourceHandle,
    #     resource: Resource
    # ) -> ResourceHandle:
    #     if handle.key in self._resources:
    #         return
        
    #     self._resources[handle.key] = await resource.load()

    #     return handle
        
    # def release(
    #     self,
    #     handle: ResourceHandle
    # ) -> Union[Resource, None]:
    #     return self._resources.pop(handle.key, None)