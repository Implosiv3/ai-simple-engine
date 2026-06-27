from ai_simple_engine.plugins.providers.abstract import PluginProvider
from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver
from abc import abstractmethod


class RuntimeValueResolverProvider(
    PluginProvider
):

    @abstractmethod
    def runtime_value_resolvers(
        self
    ) -> list[RuntimeValueResolver]:
        ...