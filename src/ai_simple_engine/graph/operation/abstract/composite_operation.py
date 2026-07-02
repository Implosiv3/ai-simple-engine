from ai_simple_engine.graph.operation.abstract.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from abc import ABC, abstractmethod


class CompositeOperation(
    Operation,
    ABC
):
    
    @abstractmethod
    def expand(
        self
    ) -> dict[str, PortReference]:
        """
        The ability to expand it into different
        operations. It doesn't exist if it is a
        simple operation.
        """
        ...