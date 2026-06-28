from dataclasses import dataclass
from ai_simple_engine.resources.resource_key import ResourceKey


@dataclass(frozen = True)
class ResourceHandle:
    
    key: ResourceKey