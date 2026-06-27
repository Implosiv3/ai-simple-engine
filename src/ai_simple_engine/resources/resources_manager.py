from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.resources.resource_handle import ResourceHandle
from uuid import UUID, uuid4
from typing import Union


class ResourceManager:

    def __init__(
        self
    ):
        self._resources: dict[UUID, object] = {}

    async def register(
        self,
        handle: ResourceHandle,
        resource: Resource
    ) -> ResourceHandle:
        if handle.id in self._resources:
            return
        
        self._resources[handle.id] = await resource.load()

        return handle
        
    def get(
        self,
        handle: ResourceHandle
    ) -> Resource:
        return self._resources[handle.id]

    def release(
        self,
        handle: ResourceHandle
    ) -> Union[Resource, None]:
        return self._resources.pop(handle.id, None)