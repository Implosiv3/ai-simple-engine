from ai_simple_engine.dependencies.utils import find_port_references
from ai_simple_engine.graph.operation.base import Operation


class DependencyFinder:
    """
    Class to simplify the way we find dependencies.
    """

    def find(
        self,
        operation: Operation
    ):
        """
        Find the dependencies of the given `operation`,
        that will be also `Operation` instances.

        This method is doing `yield`.
        """
        for reference in find_port_references(operation):
            yield reference.operation

        # return iter_dependencies(operation)