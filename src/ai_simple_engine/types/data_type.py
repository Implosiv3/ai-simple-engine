from dataclasses import dataclass
from typing import Union


@dataclass(frozen = True, slots = True)
class DataType:
    """
    Represents a type that can travel through the graph.

    Type are compared by name.
    """

    name: str
    parent: Union['DataType', None] = None

    def is_assignable_from(
        self,
        other: 'DataType'
    ) -> bool:
        current = other

        while current is not None:
            if current == self:
                return True

            current = current.parent

        return False

    def __str__(
        self
    ) -> str:
        return self.name

    def __repr__(
        self
    ) -> str:
        return f'DataType({self.name!r})'
    





"""
    -- Specific types below --
"""
TENSOR = DataType('Tensor')
IMAGE = DataType(
    'Image',
    parent = TENSOR
)
LATENT = DataType(
    'Latent',
    parent = TENSOR
)
MODEL = DataType('Model')
AUDIO = DataType('Audio')
STRING = DataType('String')
FLOAT = DataType('Float')
INT = DataType('Int')
BOOLEAN = DataType('Boolean')

