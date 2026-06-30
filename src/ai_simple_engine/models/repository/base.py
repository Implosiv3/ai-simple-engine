from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.models.backends.model_backend_registry import ModelBackendRegistry
from ai_simple_engine.models.spec.base import ModelSpec


class ModelRepository:
    """
    A repository in which we include all the
    model backends we have available, so we
    know how to obtain a model with its
    `ModelSpec`.

    This will hide the way those models are
    accesible through our app and just provide a
    way to use them.

    It can include more than one backend, which
    are the classes that can actually download
    the models from the different platforms.
    """
    
    def __init__(
        self,
        backends: ModelBackendRegistry,
    ):
        self._backends = backends

    # TODO: Is this being used (?)
    def _provider(
        self,
        spec: ModelSpec
    ) -> ModelBackend:
        try:
            return self._backends.resolve(spec)

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