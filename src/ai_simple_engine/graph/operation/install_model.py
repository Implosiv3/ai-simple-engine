from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import STRING


class InstallModel(
    Operation
):

    model = Input(STRING)

    revision = Input(
        STRING,
        optional=True
    )

    installed_model = Output(INSTALLED_MODEL)

    async def execute(self, context):

        model = await context.models.install(
            self.model,
            revision = self.revision
        )

        return {
            'installed_model': model
        }