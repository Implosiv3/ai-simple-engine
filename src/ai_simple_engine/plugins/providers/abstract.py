# from ai_simple_engine.engine_builder import EngineBuilder
from abc import ABC, abstractmethod


class PluginProvider(
    ABC
):
    
    @abstractmethod
    def register(
        self,
        builder: 'EngineBuilder'
    ) -> None:
        ...
        # builder.add_...