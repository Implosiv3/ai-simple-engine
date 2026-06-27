from ai_simple_engine.graph.graph import Graph
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.operation.composite_operation import CompositeOperation
from ai_simple_engine.graph.port_reference import PortReference
from typing import Union, Iterable


class GraphBuilder:

    def build(
        self,
        outputs: Union[PortReference, Iterable[PortReference]]
    ) -> Graph:
        if isinstance(outputs, PortReference):
            outputs = [outputs]

        operations: list[Operation] = []
        visited: set[int] = set()

        for output in outputs:
            self._visit(
                output.operation,
                operations,
                visited
            )

        return Graph(operations)
    
    def _visit(
        self,
        operation: Operation,
        operations: list[Operation],
        visited: set[int]
    ) -> None:
        if isinstance(operation, CompositeOperation):
            output = operation.build()

            self._visit(output.operation)

            return
        
        operation_id = id(operation)

        if operation_id in visited:
            return

        visited.add(operation_id)

        for dependency in self._dependencies(operation):
            self._visit(
                dependency,
                operations,
                visited
            )

        operations.append(operation)

    def _dependencies(
        self,
        operation: Operation
    ) -> list[Operation]:

        dependencies = []

        for field in operation.model_fields:

            value = getattr(operation, field)

            for reference in find_port_references(value):
                dependencies.append(reference.operation)

        return dependencies
    


# TODO: Move to a utils (?)
from collections.abc import Mapping
from collections.abc import Sequence


def find_port_references(value):
    if isinstance(value, PortReference):
        yield value
        return

    if isinstance(value, Mapping):

        for v in value.values():
            yield from find_port_references(v)

        return

    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):

        for v in value:
            yield from find_port_references(v)