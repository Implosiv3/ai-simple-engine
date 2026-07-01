from ai_simple_engine.services.keyed_service_registry import KeyedServiceRegistry
from abc import ABC, abstractmethod
from typing import Generic, TypeVar


TResolved = TypeVar('TResolved')
TService = TypeVar('TService')
TKey = TypeVar('TKey')

class ResolverRegistry(
    KeyedServiceRegistry[TKey, TService],
    Generic[TResolved, TService, TKey],
    ABC
):
    """
    Base registry that resolves a service from an object.
    """

    @abstractmethod
    def key_for(
        self,
        value: TResolved
    ) -> TKey:
        """
        Returns the registry key for the given object.
        """
        ...

    def resolve(
        self,
        value: TResolved
    ) -> TService:
        """
        Resolves the appropriate service for the given object.
        """
        return self.get(self.key_for(value))