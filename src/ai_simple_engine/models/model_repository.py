from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.models.backends.model_backend_registry import ModelBackendRegistry
from ai_simple_engine.models.model_spec import ModelSpec


class ModelRepository:
    
    def __init__(
        self,
        backends: ModelBackendRegistry,
    ):
        self._backends = backends

    def _provider(
        self,
        spec: ModelSpec
    ) -> ModelBackend:
        try:
            return  self._backends.resolve(spec)

        except KeyError:
            raise ValueError(f'Unknown model backend "{spec.provider}".')

    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        """
        Install the model with the given `spec` and
        return it as an `InstalledModel` instance.
        """
        backend = self._backends.resolve(spec)

        return await backend.install(spec)