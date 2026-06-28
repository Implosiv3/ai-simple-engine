from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.resources.resources_manager import ResourceManager
from ai_simple_engine.models.model_repository import ModelRepository
from ai_simple_engine.models.loaders.model_loader_registry import ModelLoaderRegistry
from ai_simple_engine.cache.base import Cache
from ai_simple_engine.settings.engine_settings import EngineSettings
from typing import Union
from uuid import UUID


class ExecutionContext:

    def __init__(
        self,
        settings: EngineSettings,
        model_repository: ModelRepository,
        model_loader_registry: ModelLoaderRegistry,
        resource_manager: ResourceManager,
        cache: Union[Cache, None] = None
    ):
        self.settings: EngineSettings = settings
        """
        All the internal settings of the engine.
        """

        self.models = model_repository
        """
        Access to the model repository.
        """
        self.model_loaders = model_loader_registry
        self.resources = resource_manager
        self.cache = cache
        self._operation_outputs: dict[UUID, dict[str, object]] = {}

    def has_result(
        self,
        operation: Operation
    ) -> bool:
        return operation.id in self._operation_outputs

    def store(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ) -> None:
        self._operation_outputs[operation.id] = outputs

    def outputs(
        self,
        operation: Operation
    ) -> dict[str, object]:
        return self._operation_outputs[operation.id]

    def output(
        self,
        operation: Operation,
        name: str
    ) -> object:
        return self._operation_outputs[operation.id][name]
    

from ai_simple_engine.graph.port_reference import PortReference

def result(
    self,
    reference: PortReference
):
    return self.output(
        reference.operation,
        reference.port.name
    )