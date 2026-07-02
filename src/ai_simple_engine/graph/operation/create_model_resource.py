from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.resources.model_resource import ModelResource
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import DEVICE, INSTALLED_MODEL, MODEL_RESOURCE, MODEL_LOADER
from ai_simple_engine.device.base import CUDA


class CreateModelResource(
    AtomicOperation
):
    """
    *Atomic Operation*

    Create a `ModelResource` instance with the `device`, 
    `installed_model` and `loader` provided.

    Inputs:
    - `installed_model` (`INSTALLED_MODEL`)
    - `loader` (`MODEL_LOADER`)
    - `device` (`DEVICE`)

    Outputs:
    - `model_resource` (`MODEL_RESOURCE`)
    """

    installed_model = Input(INSTALLED_MODEL)
    loader = Input(MODEL_LOADER)
    device = Input(
        type = DEVICE,
        default = CUDA
    )

    model_resource = Output(MODEL_RESOURCE)

    async def execute(
        self,
        context
    ):
        model_resource = ModelResource(
            installed_model = self.installed_model,
            loader = self.loader,
            device = self.device
        )

        return {
            'model_resource': model_resource
        }