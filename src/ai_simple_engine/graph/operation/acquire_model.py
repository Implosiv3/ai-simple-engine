from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.models.loaded_model import LoadedModel
from ai_simple_engine.types.data_type import DEVICE, INSTALLED_MODEL, LOADED_MODEL
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
        DEVICE,
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

        instance = await loader.load(
            installed_model = self.installed_model,
            device = self.device
        )

        loaded_model = LoadedModel(
            installed_model = self.installed_model,
            instance = instance
        )

        await context.resources.register(loaded_model)

        return {
            'model': loaded_model
        }