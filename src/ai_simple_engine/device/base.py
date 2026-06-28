from dataclasses import dataclass
from typing import Union


@dataclass(frozen = True)
class Device:
    """
    Represents a computation device.
    """

    identifier: str

    @property
    def type(
        self
    ) -> str:
        """
        Returns the device type ('cpu', 'cuda', 'mps'...).
        """
        return self.identifier.split(':')[0]

    @property
    def index(
        self
    ) -> Union[int, None]:
        """
        Returns the device index if present.
        """
        parts = self.identifier.split(':', 1)

        if len(parts) == 1:
            return None

        return int(parts[1])

    def __str__(
        self
    ) -> str:
        return self.identifier

    def __repr__(
        self
    ) -> str:
        return f'Device({self.identifier!r})'
    

CPU = Device('cpu')
CUDA = Device('cuda')
MPS = Device('mps')
XPU = Device('xpu')
DIRECTML = Device('directml')