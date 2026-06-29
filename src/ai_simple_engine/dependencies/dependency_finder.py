from ai_simple_engine.dependencies.utils import find_operations
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
        for reference in find_operations(operation):
            yield reference

        # return iter_dependencies(operation)