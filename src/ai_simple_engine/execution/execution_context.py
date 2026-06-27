from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.graph.operation.cache import Cache
from uuid import UUID


class ExecutionContext:

    def __init__(
        self
    ):
        self.resources = ResourceManager()
        self._results: dict[UUID, dict[str, object]] = {}
        self.cache = Cache()

    def has_result(
        self,
        operation: Operation
    ) -> bool:
        return operation.id in self._results

    def store(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ) -> None:
        self._results[operation.id] = outputs

    def outputs(
        self,
        operation: Operation
    ) -> dict[str, object]:
        return self._results[operation.id]

    def output(
        self,
        operation: Operation,
        name: str
    ) -> object:
        return self._results[operation.id][name]