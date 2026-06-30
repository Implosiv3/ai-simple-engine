from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.output import Output
from ai_simple_engine.graph.input import Input
from ai_simple_engine.resources.model_resource import ModelResource
from ai_simple_engine.types.data_type.base import RESOURCE, INSTALLED_MODEL, STRING


class LoadModel(
    Operation
):
    
    model = Input(INSTALLED_MODEL)
    device = Input(
        STRING,
        default = 'cuda'
    )
    resource = Output(RESOURCE)

    async def execute(
        self,
        context
    ):
        loader = context.model_loaders.get(self.model.family)

        handle = await context.resources.load(
            ModelResource(
                model = self.model,
                loader = loader,
                device = self.device
            )

        )

        return {
            'resource': handle
        }