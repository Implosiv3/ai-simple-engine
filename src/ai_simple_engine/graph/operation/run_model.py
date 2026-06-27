from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import MODEL, IMAGE


class RunModel(
    Operation
):

    model = Input(MODEL)
    image = Input(IMAGE)
    result = Output(IMAGE)

    async def execute(
        self,
        context
    ):
        model = context.resources.get(self.model)

        ...