from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.resources.resource_handle import ResourceHandle
from ai_simple_engine.resources.loaded_resource import LoadedResource
from ai_simple_engine.resources.resource_key import ResourceKey


class ResourceManager:

    def __init__(
        self
    ):
        self._resources: dict[ResourceKey, Resource] = {}
        self._instances: dict[ResourceKey, object]

    async def register(
        self,
        resource: Resource
    ) -> ResourceHandle:
        key = resource.key

        self._resources[key] = resource

        return ResourceHandle(key)
    
    async def resolve(
        self,
        handle: ResourceHandle
    ):
        key = handle.key

        if key not in self._instances:
            resource = self._resources[key]
            self._instances[key] = await resource.load()

        return self._instances[key]
    
    async def release(
        self,
        handle: ResourceHandle
    ):
        key = handle.key

        instance = self._instances.pop(key, None)

        if instance is None:
            return

        resource = self._resources[key]

        await resource.unload(instance)

    """
    TODO: What about all this below (?)
    """
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