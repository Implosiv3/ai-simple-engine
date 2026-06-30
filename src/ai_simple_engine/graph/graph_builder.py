from ai_simple_engine.graph.graph import Graph
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.dependencies.dependency_finder import DependencyFinder
from typing import Union, Iterable
from uuid import UUID


class GraphBuilder:
    """
    Class capable of building the `Graph`
    by using all the `targets` provided,
    that can be `Operation` or `PortReference`.
    """

    def __init__(
        self
    ):
        self._dependency_finder = DependencyFinder()

    def build(
        self,
        targets: Union[Operation, PortReference, Iterable[Union[Operation, PortReference]]]
    ) -> Graph:
        if isinstance(targets, (Operation, PortReference)):
            targets = [targets]

        operations: dict[UUID, Operation] = {}

        for target in targets:
            if isinstance(target, Operation):
                self._visit_operation(
                    operation = target,
                    operations = operations
                )
            elif isinstance(target, PortReference):
                self._visit_operation(
                    operation = target.operation,
                    operations = operations
                )
            else:
                raise TypeError(f'Unsupported target: {type(target)}')

        graph = Graph()

        for operation in operations.values():
            graph.add(operation)

        return graph
    
    def _visit_operation(
        self,
        operation: Operation,
        operations: dict[UUID, Operation]
    ) -> None:
        if operation.id in operations:
            return
        
        expanded = operation.expand()

        if expanded is not None:
            self._visit_operation(
                expanded.operation,
                operations
            )

            return

        operations[operation.id] = operation

        for dependency in self._dependency_finder.find(operation):
            self._visit_operation(
                dependency,
                operations
            )