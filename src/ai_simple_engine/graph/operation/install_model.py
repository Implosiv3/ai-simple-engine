from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import MODEL_SPEC, INSTALLED_MODEL


class InstallModel(
    Operation
):

    spec = Input(MODEL_SPEC)
    installed_model = Output(INSTALLED_MODEL)

    async def execute(
        self,
        context
    ):
        model = await context.models.install(self.spec)

        return {
            'installed_model': model
        }