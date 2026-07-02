from ai_simple_engine.resources.handle.base import ResourceHandle
from ai_simple_engine.resources.model_resource import ModelResource
from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.models.loaders.abstract import ModelLoader
from ai_simple_engine.models.spec.base import ModelSpec
from ai_simple_engine.device.base import Device
from ai_simple_engine.types.audio import Audio
from ai_simple_engine.types.image import Image
from pathlib import Path
from typing import Union, TypeVar, Generic


T = TypeVar('T')

class DataType(
    Generic[T]
):
    """
    Our engine's data type class, that defines some
    conditions but also the `runtime_type` that is
    expected.
    """
    
    runtime_type: type[T]
    """
    The python type of this data type. This can be
    used to validate it.
    """

    def __init__(
        self,
        name: str,
        runtime_type: type[T],
        parent: Union['DataType', None] = None
    ):
        self.name = name
        self.runtime_type = runtime_type
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
        if not isinstance(value, self.runtime_type):
            raise TypeError(f'Expected "{self.runtime_type.__name__}", got "{type(value).__name__}".')
        
    def schema(
        self
    ) -> dict:
        return {
            'name': self.name,
            'runtime_type': self.runtime_type.__name__
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

# Basic types
STRING = DataType(
    name = 'String',
    runtime_type = str,
    parent = None
)
FLOAT = DataType(
    name = 'Float',
    runtime_type = float,
    parent = None
)
INT = DataType(
    name = 'Int',
    runtime_type = int,
    parent = None
)
BOOLEAN = DataType(
    name = 'Boolean',
    runtime_type = bool,
    parent = None
)
# TODO: Duplicated, same as 'OBJECT'
ANY = DataType(
    name = 'Any',
    runtime_type = object,
    parent = None
)
OBJECT = DataType(
    name = 'Object',
    runtime_type = object,
    parent = None
)

# Almost basic types
PATH = DataType(
    name = 'Path',
    runtime_type = Path,
    parent = None
)

# Specific types
RESOURCE = DataType(
    name = 'Resource',
    runtime_type = ResourceHandle,
    parent = None
)
INSTALLED_MODEL = DataType(
    name = 'InstalledModel',
    runtime_type = InstalledModel,
    parent = None
)
LOADED_MODEL = DataType(
    name = 'LoadedModel',
    runtime_type = LoadedModel,
    parent = None
)
MODEL_RESOURCE = DataType(
    name = 'ModelResource',
    runtime_type = ModelResource,
    parent = None
)
MODEL_LOADER = DataType(
    name = 'ModelLoader',
    runtime_type = ModelLoader,
    parent = None
)
MODEL_SPEC = DataType(
    name = 'ModelSpec',
    runtime_type = ModelSpec,
    parent = None
)
AUDIO = DataType(
    name = 'Audio',
    runtime_type = Audio,
    parent = None
)
DEVICE = DataType(
    name = 'Device',
    runtime_type = Device,
    parent = None
)
IMAGE = DataType(
    name = 'Image',
    runtime_type = Image,
    parent = None
)

# TODO: These 3 below are in 'ai-simple-engine-diffusion'
# LATENTS = DataType(
#     name = 'Latents',
#     runtime_type = Latents,
#     parent = None
# )
# EMBEDDINGS = DataType(
#     name = 'Embeddings',
#     runtime_type = Embeddings,
#     parent = None
# )
# NOISE_PREDICTION = DataType(
#     name = 'NoisePrediction',
#     runtime_type = NoisePrediction,
#     parent = None
# )