"""
TODO: I don't know if this is an operation
or if it should be here.
"""
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import STRING, PATH


class DownloadModel(
    Operation
):

    model = Input(STRING)
    path = Output(PATH)

    async def execute(self, context):
        path = await context.models.download(
            self.model
        )

        return {
            'path': path
        }