from ai_simple_engine.execution.execution_context import ExecutionContext
from ai_simple_engine.plugins.plugin_component import PluginComponent
from abc import ABC, abstractmethod


class RuntimeValueResolver(
    PluginComponent,
    ABC
):
    """
    *Abstract class*
    
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
        """
        Check if the `value` provided is supported
        or not by the specific `RuntimeValueResolver`
        implementation.
        """
        ...

    @abstractmethod
    async def resolve(
        self,
        value: object,
        context: ExecutionContext
    ) -> object:
        """
        Resolve the `ResourceHandle` that comes as
        `value` to be able to use it. This means 
        that the resource will be loaded so it can
        be used to perform the operations.
        """
        ...