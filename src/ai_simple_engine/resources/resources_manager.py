from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.resources.resource_handle import ResourceHandle
from uuid import UUID, uuid4


class ResourceManager:

    def __init__(
        self
    ):
        self._resources: dict[UUID, Resource] = {}

    def register(
        self,
        resource: Resource
    ) -> ResourceHandle:
        handle = ResourceHandle(uuid4())

        self._resources[handle.id] = resource

        return handle

    def get(
        self,
        handle: ResourceHandle
    ) -> Resource:
        return self._resources[handle.id]

    def remove(
        self,
        handle: ResourceHandle
    ) -> None:
        del self._resources[handle.id]