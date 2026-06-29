# from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from collections.abc import Mapping, Sequence


# def iter_dependencies(
#     value
# ):
#     """
#     Iterate over the dependencies of the given `value`
#     and yield each `value.operation` when a
#     `PortReference` instance is found.
#     """
#     if isinstance(value, Operation):
#         for input_name in value.inputs():
#             input_value = getattr(value, input_name)
#             yield from iter_dependencies(input_value)
#         return

#     if isinstance(value, PortReference):
#         yield value.operation
#         return

#     if isinstance(value, Mapping):
#         for v in value.values():
#             yield from iter_dependencies(v)
#         return

#     if (
#         isinstance(value, Sequence)
#         and not isinstance(value, (str, bytes))
#     ):
#         for v in value:
#             yield from iter_dependencies(v)

def find_port_references(
    value
):
    if isinstance(value, PortReference):
        yield value
        return

    if isinstance(value, Mapping):
        for v in value.values():
            yield from find_port_references(v)
            
        return

    if (
        isinstance(value, Sequence) and
        not isinstance(value, (str, bytes))
    ):
        for v in value:
            yield from find_port_references(v)