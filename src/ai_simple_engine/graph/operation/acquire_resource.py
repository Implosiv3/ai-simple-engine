from ai_simple_engine.graph.operation.abstract.atomic_operation import AtomicOperation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type.base import RESOURCE, OBJECT


class AcquireResource(
    AtomicOperation
):
    """
    *Atomic Operation*

    Acquire the `Resource` provided as input and
    get the instance of it.

    Inputs:
    - `resource` (`RESOURCE`)

    Outputs:
    - `instance` (`OBJECT`)
    """
    
    resource = Input(RESOURCE)

    instance = Output(OBJECT)

    async def execute(
        self,
        context
    ):
        instance = await context.resources.acquire(self.resource)

        return {
            'instance': instance
        }