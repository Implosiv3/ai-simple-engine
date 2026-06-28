from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.resources.music_gen_resource import MusicGenResource
from ai_simple_engine.types.data_type import INSTALLED_MODEL, STRING, RESOURCE


class LoadMusicGenModel(
    Operation
):

    path = Input(INSTALLED_MODEL)
    device = Input(
        type = STRING,
        default = 'cuda'
    )
    model = Output(RESOURCE)

    async def execute(
        self,
        context
    ):
        handle = await context.resources.load(
            MusicGenResource(
                self.path,
                self.device
            )
        )

        return {
            'model': handle
        }