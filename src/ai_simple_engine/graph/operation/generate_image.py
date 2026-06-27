from ai_simple_engine.graph.operation.composite_operation import CompositeOperation
from ai_simple_engine.graph.operation.load_model import LoadModel
from ai_simple_engine.graph.output import Output
from ai_simple_engine.types.data_type import IMAGE


# TODO: This will be in a specific module/library
# TODO: Handle this
class Sample:
    ...

class Decode:
    ...

class EncodePrompt:
    ...


class GenerateImage(
    CompositeOperation
):

    prompt: str

    image = Output(IMAGE)

    @classmethod
    def build(cls):

        model = LoadModel(...)

        # TODO: How do we handle this (?)
        conditioning = EncodePrompt(
            prompt=cls.prompt
        )

        latent = Sample(
            model=model.model,
            conditioning=conditioning.conditioning
        )

        return Decode(
            latent=latent.latent
        ).image