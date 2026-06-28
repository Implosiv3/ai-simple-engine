from dataclasses import dataclass


@dataclass(frozen = True)
class Device:
    """
    Represents a computation device.
    """

    identifier: str

    def __str__(
        self
    ) -> str:
        return self.identifier

    def __repr__(
        self
    ) -> str:
        return f'Device({self.identifier!r})'