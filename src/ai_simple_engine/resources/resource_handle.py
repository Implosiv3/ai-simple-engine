from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen = True)
class ResourceHandle:
    
    key: str