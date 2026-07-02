from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import INSTALLED_MODEL, MODEL_LOADER


class ResolveModelLoader(
    AtomicOperation
):
    """
    *Atomic Operation*

    Resolve (and get) the `ModelLoader` that is
    in charge of loading the `installed_model`
    given.

    Inputs:
    - `installed_model` (`INSTALLED_MODEL`)

    Outputs:
    - `loader` (`MODEL_LOADER`)
    """
    
    installed_model = Input(INSTALLED_MODEL)

    loader = Output(MODEL_LOADER)

    async def execute(
        self,
        context
    ):
        loader = context.model_loaders.resolve(self.installed_model)

        return {
            'loader': loader
        }