from ai_simple_engine.resources.builder.abstract import ResourceBuilder
from ai_simple_engine.resources.model_resource import ModelResource
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.device.base import Device
from typing import Union


# TODO: Is this being used (?)
class ModelResourceBuilder(
    ResourceBuilder
):

    def is_supported(
        self,
        value
    ):
        return isinstance(value, LoadedModel)

    def create(
        self,
        value: object,
        *,
        device: Union[Device, None]
    ) -> ModelResource:
        return ModelResource(...)