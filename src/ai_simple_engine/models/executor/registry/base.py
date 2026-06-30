from ai_simple_engine.services.keyed_service_registry import KeyedServiceRegistry
from abc import ABC, abstractmethod
from typing import Generic, TypeVar


TModel = TypeVar('TModel')
TRunner = TypeVar('TRunner')
TKey = TypeVar('TKey')

class ModelExecutorRegistry(
    KeyedServiceRegistry[TKey, TRunner],
    Generic[TModel, TRunner, TKey],
    ABC
):
    """
    Base registry capable of resolving the correct
    `ModelExecutor` for a given model.
    """

    @abstractmethod
    def key_for(
        self,
        model: TModel
    ) -> TKey:
        """
        Returns the registry key that should be used
        for the supplied model.
        """
        ...

    def resolve(
        self,
        model: TModel
    ) -> TRunner:
        """
        Resolves the appropriate runner for a model.
        """
        return self.get(self.key_for(model))