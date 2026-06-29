from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from collections.abc import Mapping, Sequence
from hashlib import sha256
from typing import Protocol, Any


class OperationFingerprintBuilder:
    """
    Class to build fingerprints of operations.
    """

    @staticmethod
    def _serialize(
        value: Any,
        visited: set
    ) -> bytes:
        if isinstance(value, PortReference):
            return OperationFingerprintBuilder._build(
                value.operation,
                visited
            ).encode()

        if isinstance(value, Mapping):
            data = b""

            for key in sorted(value):
                data += key.encode()
                data += OperationFingerprintBuilder._serialize(
                    value[key],
                    visited
                )

            return data

        if (
            isinstance(value, Sequence)
            and not isinstance(value, (str, bytes))
        ):

            data = b""

            for item in value:
                data += OperationFingerprintBuilder._serialize(
                    item,
                    visited
                )

            return data

        return repr(value).encode()

    @staticmethod
    def _build(
        operation: Operation,
        visited: set
    ) -> str:
        if operation in visited:
            return str(operation.id)

        visited.add(operation)

        hasher = sha256()
        hasher.update(operation.__class__.__qualname__.encode())

        for input_name, _ in sorted(operation.inputs().items()):
            value = getattr(operation, input_name)
            hasher.update(input_name.encode())
            hasher.update(
                OperationFingerprintBuilder._serialize(
                    value = value,
                    visited = visited
                )
            )

        return hasher.hexdigest()
    
    @staticmethod
    def build(
        operation: Operation
    ) -> str:
        return OperationFingerprintBuilder._build(operation, set())
    


# TODO: Maybe move to another file (?)
class Fingerprintable(
    Protocol
):
    def fingerprint(
        self
    ) -> bytes: ...
    
