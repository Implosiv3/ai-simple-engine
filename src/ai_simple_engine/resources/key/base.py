from dataclasses import dataclass
from typing import Union


# TODO: Refactor the use of it
@dataclass(frozen = True)
class ResourceKey:
    """
    Class to identify a resolve a unique key that
    identifies a resource so we avoid instantiating
    the same resource twice if we already have it.
    """

    category: str
    identifier: str
    variant: Union[str, None] = None