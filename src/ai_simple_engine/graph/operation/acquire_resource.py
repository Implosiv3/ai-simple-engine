from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import RESOURCE_HANDLE, OBJECT


class AcquireResource(
    AtomicOperation
):
    """
    *Atomic Operation*

    Acquire an instance of the `Resource` associated
    to the `ResourceHandle` given as `resource_handle`
    input. This will perform a `load` operation if the
    resource was not previously load in the system.

    Inputs:
    - `resource_handle` (`RESOURCE_HANDLE`)

    Outputs:
    - `instance` (`OBJECT`)
    """
    
    resource_handle = Input(RESOURCE_HANDLE)

    resource = Output(OBJECT)

    async def execute(
        self,
        context
    ):
        instance = await context.resources.resolve(self.resource_handle)

        return {
            'instance': instance
        }