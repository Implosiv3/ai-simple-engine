from ai_simple_engine.models.executor.registry.base import ModelExecutorRegistry
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.models.executor.abstract import ModelExecutor
from typing import Generic, TypeVar


TModel = TypeVar('TModel', bound = LoadedModel)
TExecutor = TypeVar('TExecutor', bound = ModelExecutor)

class FamilyModelExecutorRegistry(
    ModelExecutorRegistry[
        TModel,
        TExecutor,
        str
    ],
    Generic[TModel, TExecutor]
):
    """
    A `ModelExecutor` registry that uses the model's
    `family` as the key (`key_for`).
    """

    def key_for(
        self,
        model: TModel
    ) -> str:
        return model.installed_model.family