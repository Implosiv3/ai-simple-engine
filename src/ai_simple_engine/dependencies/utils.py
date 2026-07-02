from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.graph.operation.abstract.base import Operation
from collections.abc import Mapping, Sequence


"""
TODO: Do I need to change something here
due to the new 'AtomicOperation' and
'CompositeOperation' (?)
"""
def find_operations(
    operation: Operation
):
    """
    Iterate over the inputs of the `operation`
    given to find other operations recursively,
    yielding all the ones that are found.
    """
    for input_name in operation.inputs():
        value = getattr(operation, input_name)
        yield from _find(value)

def _find(
    value
):
    """
    *For internal use only*

    Find the `PortReference` instances and
    yield its `.operation` attribute.
    """
    if isinstance(value, PortReference):
        yield value.operation
        return

    if isinstance(value, Mapping):
        for v in value.values():
            yield from _find(v)
        return

    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        for v in value:
            yield from _find(v)