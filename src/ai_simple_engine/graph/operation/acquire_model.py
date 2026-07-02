from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.resources.model_resource import ModelResource
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import DEVICE, INSTALLED_MODEL, LOADED_MODEL
from ai_simple_engine.device.base import CUDA


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
        type = DEVICE,
        default = CUDA
    )
    model = Output(LOADED_MODEL)
    """
    The `LoadedModel` that will become as the model
    acquired.
    """

    async def execute(
        self,
        context
    ):
        loader = context.model_loaders.resolve(self.installed_model)

        """
        The specific loader will load the specific
        model (and its info) and return that instance.
        """
        loaded_model = await loader.load(
            installed_model = self.installed_model,
            device = self.device
        )

        await context.resources.acquire(
            ModelResource(
                model = loaded_model,
                loader = loader,
                device = self.device
            )
        )

        return {
            'model': loaded_model
        }