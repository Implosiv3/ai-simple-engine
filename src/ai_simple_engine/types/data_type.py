from ai_simple_engine.resources.resource_handle import ResourceHandle
from pathlib import Path
from typing import Union, TypeVar, Generic


T = TypeVar('T')

class DataType(
    Generic[T]
):
    """
    Our engine's data type class, that defines some
    conditions but also the `python_type` that is
    expected.
    """
    
    python_type: type[T]
    """
    The python type of this data type. This can be
    used to validate it.
    """

    def __init__(
        self,
        name: str,
        python_type: type[T],
        parent: Union['DataType', None] = None
    ):
        self.name = name
        self.python_type = python_type
        self.parent = parent

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
    
    def validate(
        self,
        value: object
    ) -> None:
        if not isinstance(value, self.python_type):
            raise TypeError(f'Expected "{self.python_type.__name__}", got "{type(value).__name__}".')
        
    def schema(
        self
    ) -> dict:
        return {
            'name': self.name,
            'python_type': self.python_type.__name__
        }
    
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
TENSOR = DataType(
    name = 'Tensor',
    python_type = 'torch.Tensor', # torch.Tensor, but I don't want import
    parent = None
)
IMAGE = DataType(
    name = 'Image',
    python_type = 'PIL.Image.Image', # PIL.Image.Image, but I don't want import
    parent = TENSOR
)
LATENT = DataType(
    name = 'Latent',
    python_type = 'torch.Tensor', # torch.Tensor, but I don't want import
    parent = TENSOR
)
MODEL = DataType(
    name = 'Model',
    python_type = ResourceHandle,
    parent = None
)
AUDIO = DataType(
    name = 'Audio',
    python_type = 'np.ndarray', # np.ndarray, but i don't want import
    parent = None # TODO: TENSOR maybe (?)
)
# TODO: Review this type because I'm not sure
PATH = DataType(
    name = 'Path',
    python_type = Path,
    parent = None
)
STRING = DataType(
    name = 'String',
    python_type = str,
    parent = None
)
FLOAT = DataType(
    name = 'Float',
    python_type = float,
    parent = None
)
INT = DataType(
    name = 'Int',
    python_type = int,
    parent = None
)
BOOLEAN = DataType(
    name = 'Boolean',
    python_type = bool,
    parent = None
)
ANY = DataType(
    name = 'any',
    python_type = object,
    parent = None
)
# TODO: Review this:
INSTALLED_MODEL = DataType(
    name = 'installed_model',
    python_type = ResourceHandle,
    parent = None
)
