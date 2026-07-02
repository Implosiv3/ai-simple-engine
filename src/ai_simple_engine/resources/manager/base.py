from ai_simple_engine.resources.abstract import Resource
from ai_simple_engine.resources.handle.base import ResourceHandle
from ai_simple_engine.resources.key.base import ResourceKey


class ResourceManager:
    """
    Class to handle the different resources and
    their instances.
    """

    def __init__(
        self
    ):
        self._resources: dict[ResourceKey, Resource] = {}
        self._instances: dict[ResourceKey, object] = {}

    async def register(
        self,
        resource: Resource
    ) -> ResourceHandle:
        """
        Register the `resource` provided, if not
        registered, and return a `ResourceHandle`
        instance with its `key`.
        """
        key = resource.key

        self._resources.setdefault(
            key,
            resource
        )

        return ResourceHandle(key)
    
    async def resolve(
        self,
        handle: ResourceHandle
    ):
        """
        Try to find the instance of the `Resource`
        associated to the `key` that is in the
        `handle` given, or load the resource, creating
        the first instance, and return it.

        From `ResourceHandle` to `Resource` instance.
        """
        key = handle.key

        if key in self._instances:
            return self._instances[key]

        resource = self._resources[key]

        instance = await resource.load()

        self._instances[key] = instance

        return instance

    async def release_all(
        self
    ) -> None:
        """
        Release all the instances and the resources
        register. This must be called by the
        Executor when the whole execution has
        finished.
        """
        for key in list(self._instances):
            resource = self._resources[key]
            instance = self._instances[key]

            if instance is not None:
                # await resource.unload(instance)
                await resource.unload()

        self._instances.clear()
        self._resources.clear()