from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.types.data_type.base import INT


class Add(
    Operation
):

    INPUTS = {
        'a': INT,
        'b': INT,
    }

    OUTPUTS = {
        'result': INT,
    }

    async def execute(
        self,
        a,
        b
    ):

        return {
            'result': a + b
        }