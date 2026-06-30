from dataclasses import dataclass
from ai_simple_engine.resources.key.base import ResourceKey


@dataclass(frozen = True)
class ResourceHandle:
    """
    A representation (identifier) of a resource
    to be passed through the different nodes 
    without passing the whole object.

    This will be sent to the `ResourcesManager`
    to acquire, load or release them on demand.

    The `ResourceHandle` will be transformed into
    a `Resource`, and then loaded, obtaining an
    instance of many different classes depending
    on the type of resource.
    """
    
    key: ResourceKey