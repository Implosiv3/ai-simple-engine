from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import DEVICE, INSTALLED_MODEL, RESOURCE
from ai_simple_engine.resources.model_resource import ModelResource


class AcquireModel(
    Operation
):

    installed_model = Input(INSTALLED_MODEL)
    device = Input(
        DEVICE,
        default = 'cuda'
    )
    loaded_model = Output(RESOURCE)

    async def execute(
        self,
        context
    ):
        loader = context.model_loaders.get(
            self.installed_model.family
        )

        handle = await context.resources.register(
            ModelResource(
                model = self.installed_model,
                loader = loader,
                device = self.device
            )
        )

        return {
            'loaded_model': handle
        }