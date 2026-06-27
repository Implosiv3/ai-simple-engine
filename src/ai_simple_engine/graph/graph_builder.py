from ai_simple_engine.graph.graph import Graph
from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from typing import Union, Iterable, Mapping, Sequence
from uuid import UUID


class GraphBuilder:

    def build(
        self,
        targets: Union[Operation, PortReference, Iterable[Union[Operation, PortReference]]]
    ) -> Graph:
        if isinstance(targets, (Operation, PortReference)):
            targets = [targets]

        operations: dict[UUID, Operation] = {}

        for target in targets:
            if isinstance(target, Operation):
                self._visit_operation(target, operations)
            elif isinstance(target, PortReference):
                self._visit_operation(target.operation, operations)
            else:
                raise TypeError(f'Unsupported target: {type(target)}')

        return Graph(
            list(operations.values())
        )
    
    def _visit_operation(
        self,
        operation: Operation,
        operations: dict[UUID, Operation]
    ):
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

        for value in operation._connections.values():
            self._visit_value(
                value,
                operations
            )

    def _visit_value(
        self,
        value,
        operations: dict[UUID, Operation]
    ):
        if isinstance(value, PortReference):
            self._visit_operation(
                value.operation,
                operations
            )

            return

        if isinstance(value, Mapping):
            for item in value.values():
                self._visit_value(item, operations)

            return

        if (
            isinstance(value, Sequence) and
            not isinstance(value, (str, bytes))
        ):
            for item in value:
                self._visit_value(item, operations)