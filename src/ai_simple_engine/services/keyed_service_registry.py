from typing import Generic, TypeVar


T = TypeVar('T')

class KeyedServiceRegistry(
    Generic[T]
):

    def __init__(
        self
    ):
        self._services: dict[str, T] = {}

    def register(
        self,
        key: str,
        service: T
    ) -> None:
        if key in self._services:
            raise ValueError(
                f'Service "{key}" is already registered.'
            )

        self._services[key] = service

    def get(
        self,
        key: str
    ) -> T:
        try:
            return self._services[key]

        except KeyError:
            raise LookupError(
                f'No service registered with key "{key}".'
            )

    def has(
        self,
        key: str
    ) -> bool:
        return key in self._services

    def values(
        self,
    ) -> list[T]:
        return list(self._services.values())