from dataclasses import dataclass
from typing import Union


@dataclass(frozen = True)
class ResourceKey:
    """
    Class to identify a resolve a unique key that
    identifies a resource so we avoid instantiating
    the same resource twice if we already have it.
    """

    type: str
    identifier: str
    device: Union[str, None] = None