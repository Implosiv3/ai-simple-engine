from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.input import Input
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import IMAGE
from pydantic import Field


# TODO: This has to be in the specific operations module
class Blur(
    Operation
):
    radius: int = Field(
        default = 10,
        ge = 0
    )
    image = Input(IMAGE, name = 'image')
    result = Output(IMAGE)

    async def execute(
        self,
        context
    ):
        # TODO: Implement this
        def blur(image, radius):
            return {
                'result': image
            }
            """
            TODO: This is using PIL, but the operations
            and the code to perform will be in another
            library. The engine will be agnostic
            """
            return {
                'result': self.image.filter(
                    ImageFilter.GaussianBlur(self.radius)
                )
            }
        
        blurred = blur(
            self.image,
            self.radius
        )

        return self.Outputs(
            result = blurred
        )