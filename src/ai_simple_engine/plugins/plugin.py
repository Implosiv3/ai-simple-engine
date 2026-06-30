from abc import ABC, abstractmethod


class Plugin(
    ABC
):
    """
    *Abstract class*

    Class to include all the operations, model
    backends, data types, operations, etc. that
    this plugin (extra functionality) includes.
    """
    
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
