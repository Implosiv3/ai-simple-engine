from ai_simple_engine.graph.operation.abstract.composite_operation import CompositeOperation
from ai_simple_engine.graph.operation.resolve_model_loader import ResolveModelLoader
from ai_simple_engine.graph.operation.acquire_resource import AcquireResource
from ai_simple_engine.graph.operation.create_model_resource import CreateModelResource
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import DEVICE, INSTALLED_MODEL, LOADED_MODEL
from ai_simple_engine.device.base import CUDA


class AcquireModel(
    CompositeOperation
):
    """
    *Composite Operation*

    Receives an `installed_model` (a `InstalledModel` instance)
    and a `device` and returns a `model` output (a `LoadedModel`
    instance).

    Inputs:
    - `installed_model` (`INSTALLED_MODEL`)
    - `device` (`DEVICE`)

    Outputs:
    - `model` (`LOADED_MODEL`)
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

    def expand(
        self
    ):
        loader = ResolveModelLoader(installed_model = self.installed_model)

        model_resource = CreateModelResource(
            model = self.installed_model,
            loader = loader.loader,
            device = self.device
        )

        loaded_model = AcquireResource(
            resource = model_resource.model_resource
        )

        return {
            'model': loaded_model.instance
        }