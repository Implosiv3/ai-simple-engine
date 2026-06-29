from abc import ABC, abstractmethod


class Plugin(
    ABC
):
    
    @abstractmethod
    def register(
        self,
        builder: 'EngineBuilder'
    ) -> list:
        """
        Register the plugin elements with the `builder`
        given as parameter. The next things must be
        included:
        - Operations
        - Model Backends
        - Model Loaders
        - Data Types
        - Runtime Value Resolvers
        - ModelExecutor Registry Services
        """
        ...
