from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import AUDIO, STRING, MODEL


class GenerateMusic(
    Operation
):

    model = Input(MODEL)
    prompt = Input(STRING)
    audio = Output(AUDIO)

    async def execute(
        self,
        context
    ):
        audio = self.model.generate(
            self.prompt
        )

        return {
            'audio': audio
        }