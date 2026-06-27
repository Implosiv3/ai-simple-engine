from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.types.data_type import IMAGE


class LoadImage(
    Operation
):

    OUTPUTS = {
        'image': IMAGE
    }

    def __init__(
        self,
        path
    ):
        super().__init__(
            path = path
        )

    async def execute(
        self,
        context
    ):
        # TODO: Load the image
        image = ...

        return {
            'image': image
        }