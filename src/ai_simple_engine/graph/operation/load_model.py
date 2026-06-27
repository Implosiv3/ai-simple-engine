from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import MODEL


class LoadModel(
    Operation
):

    path: str
    model = Output(MODEL)

    async def execute(
        self,
        context
    ):
        # TODO: This has to be defined
        def load_unet(path):
            raise Exception('"load_unet" not defined')
        
        # TODO: Where do we get this from (?)
        unet = load_unet(self.path)
        handle = context.resources.register(unet)

        return {
            'model': handle
        }