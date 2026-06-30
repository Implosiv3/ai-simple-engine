from typing import Generic, TypeVar


TKey = TypeVar('TKey')
TService = TypeVar('TService')

class KeyedServiceRegistry(
    Generic[TKey, TService]
):

    def __init__(
        self
    ):
        self._services: dict[TKey, TService] = {}

    def register(
        self,
        key: TKey,
        service: TService
    ) -> None:
        if key in self._services:
            raise ValueError(f'Service "{key}" is already registered.')

        self._services[key] = service

    def get(
        self,
        key: TKey
    ) -> TService:
        try:
            return self._services[key]
        except KeyError:
            raise LookupError(f'No service registered with key "{key}".')

    def has(
        self,
        key: TKey
    ) -> bool:
        return key in self._services

    def values(
        self
    ) -> list[TService]:
        return list(self._services.values())

    def keys(
        self
    ) -> list[TKey]:
        return list(self._services.keys())

    def items(
        self
    ) -> list[tuple[TKey, TService]]:
        return list(self._services.items())
    
    # TODO: This below is not needed apparently, but...
    # def remove(
    #     self,
    #     key: TKey
    # ) -> None:
    #     self._services.pop(
    #         key,
    #         None
    #     )

    # def clear(
    #     self
    # ) -> None:
    #     self._services.clear()