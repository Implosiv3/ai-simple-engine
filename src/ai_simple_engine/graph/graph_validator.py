from ai_simple_engine.graph.graph import Graph
from ai_simple_engine.graph.port_reference import PortReference


class GraphValidator:
    """
    Class to validate all the operations of a
    `Graph`: the types, the references,
    the inputs provided, etc.
    """

    def validate(
        self,
        graph: Graph
    ) -> None:
        self._validate_inputs(graph)
        self._validate_types(graph)

    def _validate_inputs(
        self,
        graph: Graph
    ):
        for operation in graph.operations:
            for name, input in operation.inputs().items():
                if input.is_optional:
                    continue

                if not hasattr(operation, name):
                    raise ValueError(f'{operation.__class__.__name__}.{name} is missing.')

                value = getattr(operation, name)

                if value is None:
                    raise ValueError(f'{operation.__class__.__name__}.{name} is required.')
                
    def _validate_types(
        self,
        graph: Graph
    ):
        for operation in graph.operations:
            for name, input in operation.inputs().items():
                value = getattr(operation, name)

                if value is None:
                    continue

                if not isinstance(value, PortReference):
                    continue

                if not input.type.is_assignable_from(value.type):
                    raise TypeError(
                        f'{operation.__class__.__name__}.{name} '
                        f'expects {input.type} '
                        f'but got {value.type}'
                    )
                
    def _validate_reference(
        self,
        reference: PortReference
    ):
        outputs = reference.operation.outputs()

        if reference.name not in outputs:
            raise ValueError(
                f'Operation '
                f'{reference.operation.__class__.__name__} '
                f'does not declare output '
                f'{reference.name}'
            )