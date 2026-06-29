from typing import TypeVar


T = TypeVar('T')

class ServiceRegistry:
    """
    The registry that includes all the services we
    will need to use and are shared in between the
    components.
    """

    def __init__(
        self
    ):
        self._services: dict[type, object] = {}

    def register(
        self,
        service_type: type[T],
        service: T
    ) -> None:
        self._services[service_type] = service

    def get(
        self,
        service_type: type[T]
    ) -> T:
        try:
            return self._services[service_type]

        except KeyError:
            raise KeyError(
                f'Service "{service_type.__name__}" is not registered.'
            )

    def has(
        self,
        service_type: type
    ) -> bool:
        return service_type in self._services

    def remove(
        self,
        service_type: type
    ) -> None:
        self._services.pop(
            service_type,
            None
        )

    def clear(
        self
    ) -> None:
        self._services.clear()