from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import RESOURCE_HANDLE, LOADED_MODEL


class LoadModelResource(
    AtomicOperation
):
    """
    *Atomic Operation*

    Acquire an instance of the `ModelResource` 
    associated to the `ResourceHandle` given as
    `resource_handle` input. This will perform a
    `load` operation if the model resource was
    not previously load in the system.

    Inputs:
    - `resource_handle` (`RESOURCE_HANDLE`)

    Outputs:
    - `loaded_model` (`LOADED_MODEL`)
    """
    
    resource_handle = Input(RESOURCE_HANDLE)

    loaded_model = Output(LOADED_MODEL)

    async def execute(
        self,
        context
    ):
        loaded_model = await context.resources.resolve(self.resource_handle)

        return {
            'loaded_model': loaded_model
        }