from ai_simple_engine.models.backends.abstract import ModelBackend
from ai_simple_engine.models.spec.base import ModelSpec
from ai_simple_engine.resolver_registry import ResolverRegistry


class ModelBackendRegistry(
    ResolverRegistry[
        ModelSpec,
        ModelBackend,
        str
    ]
):

    def key_for(
        self,
        spec: ModelSpec
    ) -> str:
        return spec.provider