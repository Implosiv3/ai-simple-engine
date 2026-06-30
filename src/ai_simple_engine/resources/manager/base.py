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
        self._references: dict[ResourceKey, int] = {}

    async def register(
        self,
        resource: Resource
    ) -> None:
        """
        Register the given `resource` in the internal
        resources list if it was not registered before.
        """
        self._resources.setdefault(
            resource.key,
            resource
        )

    async def acquire(
        self,
        resource: Resource
    ) -> ResourceHandle:
        """
        Acquire the given `resource` from the internal
        list. This method will register if it was not
        already registered.

        This method will decrease the reference to
        that resource by 1, and remove it if the
        number of references reaches 0.

        This method will return a `ResourceHandle`
        instance.
        """
        await self.register(resource)

        resource = self._resources[resource.key]

        self._increment_references(resource.key)

        return ResourceHandle(resource.key)

    async def register(
        self,
        resource: Resource
    ) -> ResourceHandle:
        """
        Register the `resource` provided by using its
        internal key.
        
        This will increate the reference to that
        resource by 1.
        """
        key = resource.key

        self._resources[key] = resource

        return ResourceHandle(key)
    
    async def resolve(
        self,
        handle: ResourceHandle
    ):
        """
        Get the `Resource` instance associated to
        the `ResourceHandle` given as `handle` and
        load the resource by calling its `.load()`
        method.

        This method will return a loaded instance
        of this resource (could have been loaded
        before by another call).
        """
        resource = self._resources[handle.key]

        return await resource.load()

    async def release(
        self,
        handle: ResourceHandle
    ) -> 'ResourceManager':
        """
        Try to release the resource with the given
        `handle`, which means that the internal
        instance will be unloaded only if there are
        no more references to it.

        This method will decrease the reference to
        that resource by 1, and remove it if the
        number of references reaches 0.
        """
        resource = self._resources.get(handle.key)

        if resource is None:
            return self
        
        if self._decrement_references(handle.key) == 0:
            await resource.unload()

            del self._resources[handle.key]

        return self
        
    def _increment_references(
        self,
        key: ResourceKey
    ) -> int:
        """
        *For internal use only*

        Increase by one the references counter of the
        resource with the given `handle`.
        
        This method will return the number of referneces
        after the update.
        """
        references = self._references.get(key, 0) + 1
        self._references[key] = references

        return references

    def _decrement_references(
        self,
        key: ResourceKey
    ) -> 'ResourceManager':
        """
        *For internal use only*

        Decrease by one the references counter of the
        resource with the given `handle`.

        This method will return the number of referneces
        after the update.

        This method will raise an exception if the `key`
        provided was not registered.
        """
        references = self._references.get(key)

        if references is None:
            raise KeyError(
                f'Resource "{key}" is not registered.'
            )

        references -= 1

        if references <= 0:
            del self._references[key]
            return 0

        self._references[key] = references

        return references