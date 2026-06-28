from ai_simple_engine.models.installed_model import InstalledModel
from dataclasses import dataclass
from typing import TypeVar


T = TypeVar('T')


@dataclass(frozen = True)
class LoadedModel(T):
# class LoadedModel[T]:

    installed_model: InstalledModel
    instance: T