from ai_simple_engine.models.providers.abstract import ModelProvider
from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.models.installed_model import InstalledModel


class HuggingFaceModelProvider(
    ModelProvider
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