from ai_simple_engine.graph.graph import Graph
from ai_simple_engine.execution.execution_plan import ExecutionPlan
from ai_simple_engine.execution.execution_node import ExecutionNode
from collections import deque


class ExecutionPlanner:

    def build(
        self,
        graph: Graph
    ) -> ExecutionPlan:
        execution_nodes = {
            operation: ExecutionNode(operation)
            for operation in graph.operations
        }

        for node in execution_nodes.values():
            for dependency in self._dependencies(node.operation):
                dependency_node = execution_nodes[dependency]

                node.dependencies.append(dependency_node)
                dependency_node.dependents.append(node)

        ordered = self._topological_sort(
            list(execution_nodes.values())
        )

        return ExecutionPlan(ordered)
    
    def _topological_sort(
        self,
        nodes: list[ExecutionNode]
    ):
        indegree = {
            node: len(node.dependencies)
            for node in nodes
        }

        queue = deque(
            node
            for node in nodes
            if indegree[node] == 0
        )

        ordered = []

        while queue:
            node = queue.popleft()
            ordered.append(node)

            for dependent in node.dependents:
                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    queue.append(dependent)

        if len(ordered) != len(nodes):
            raise RuntimeError(
                "Cycle detected."
            )

        return ordered