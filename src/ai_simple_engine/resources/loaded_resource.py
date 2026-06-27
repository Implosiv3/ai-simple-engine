from ai_simple_engine.resources.resource import Resource
from dataclasses import dataclass


@dataclass
class LoadedResource:

    resource: Resource
    instance: object
    references: int = 1