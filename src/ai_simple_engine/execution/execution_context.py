from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.cache.base import Cache
from typing import Union
from uuid import UUID


class ExecutionContext:

    def __init__(
        self,
        resource_manager: Union[ResourceManager, None] = None,
        cache: Union[Cache, None] = None
    ):
        self.resources = (
            resource_manager
            if resource_manager is not None else
            ResourceManager()
        )
        self.cache = (
            cache
            if cache is not None else
            Cache()
        )
        self._outputs: dict[UUID, dict[str, object]] = {}

    def has_result(
        self,
        operation: Operation
    ) -> bool:
        return operation.id in self._outputs

    def store(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ) -> None:
        self._outputs[operation.id] = outputs

    def outputs(
        self,
        operation: Operation
    ) -> dict[str, object]:
        return self._outputs[operation.id]

    def output(
        self,
        operation: Operation,
        name: str
    ) -> object:
        return self._outputs[operation.id][name]