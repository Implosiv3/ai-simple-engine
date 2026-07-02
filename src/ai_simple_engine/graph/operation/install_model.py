from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import MODEL_SPEC, INSTALLED_MODEL


class InstallModel(
    AtomicOperation
):
    """
    *Atomic Operation*
    
    Install the model with the given `spec`.

    Inputs:
    - `spec` (`MODEL_SPEC`)

    Outputs:
    - `installed_model` (`INSTALLED_MODEL`)
    """

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