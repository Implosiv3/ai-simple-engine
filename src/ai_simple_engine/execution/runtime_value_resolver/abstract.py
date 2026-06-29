from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class RuntimeValueResolver(
    PluginComponent,
    ABC
):
    """
    Class to resolve special values into real values
    that can be used by the nodes, using not any model.
    Here you have some examples:

    ```
    GenerateMusic(model=AcquireModel(...))  =>  InstalledModel(...)
    CurrentDate(...)  =>  'YYYY-MM-DD'
    Device(...)  =>  'cuda:0'
    ```
    """

    @abstractmethod
    def is_supported(
        self,
        value: object
    ) -> bool:
        ...

    @abstractmethod
    async def resolve(
        self,
        value: object,
        context: ExecutionContext
    ) -> object:
        ...