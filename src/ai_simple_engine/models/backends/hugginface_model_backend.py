from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.models.installed_model import InstalledModel


class HuggingFaceModelBackend(
    ModelBackend
):

    @property
    def name(
        self
    ):
        return 'huggingface'

    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...