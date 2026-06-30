from ai_simple_engine.services.keyed_service_registry import KeyedServiceRegistry
from typing import TypeVar


T = TypeVar('T')

class ServiceRegistry(
    KeyedServiceRegistry[type[T], type[T]]
):
    """
    Registry whose keys are Python types. It will
    provide the service registered for that Python
    type.
    """

    def register(
        self,
        service_type: type[T],
        service: T
    ) -> None:
        super().register(
            key = service_type,
            service = service
        )

    def get(
        self,
        service_type: type[T]
    ) -> T:
        return super().get(service_type)

    def has(
        self,
        service_type: type[T]
    ) -> bool:
        return super().has(service_type)