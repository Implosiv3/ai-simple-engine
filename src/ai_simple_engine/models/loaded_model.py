from ai_simple_engine.models.installed_model import InstalledModel
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')


@dataclass(frozen = True)
class LoadedModel(Generic[T]):

    installed_model: InstalledModel
    instance: T