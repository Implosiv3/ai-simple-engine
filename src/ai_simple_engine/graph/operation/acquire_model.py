from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import DEVICE, INSTALLED_MODEL, RESOURCE
from ai_simple_engine.device.base import CUDA
from ai_simple_engine.resources.model_resource import ModelResource


class AcquireModel(
    Operation
):
    """
    Receives an `installed_model` (a `InstalledModel` instance)
    and a `device` and returns a `model` output (a `LoadedModel`
    instance).
    """

    installed_model = Input(INSTALLED_MODEL)
    device = Input(
        DEVICE,
        default = CUDA
    )
    model = Output(RESOURCE)
    """
    The `LoadedModel` that will become as the model
    acquired.
    """

    async def execute(
        self,
        context
    ):
        loader = context.model_loaders.resolve(self.installed_model)

        handle = await context.resources.register(
            ModelResource(
                model = self.model,
                loader = loader,
                device = self.device
            )
        )

        return {
            'model': handle
        }