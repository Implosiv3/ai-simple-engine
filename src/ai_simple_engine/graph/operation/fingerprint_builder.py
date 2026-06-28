from ai_simple_engine.graph.operation.base import Operation
from ai_simple_engine.graph.port_reference import PortReference
from collections.abc import Mapping, Sequence
from hashlib import sha256
from typing import Protocol, Any


class FingerprintBuilder:

    @staticmethod
    def _serialize(
        value: Any,
        visited: set
    ) -> bytes:
        if isinstance(value, PortReference):
            return FingerprintBuilder._build(
                value.operation,
                visited
            ).encode()

        if isinstance(value, Mapping):
            data = b""

            for key in sorted(value):
                data += key.encode()
                data += FingerprintBuilder._serialize(
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
                data += FingerprintBuilder._serialize(
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

        hasher.update(
            operation.__class__.__qualname__.encode()
        )

        for field in sorted(operation.model_fields):

            value = getattr(operation, field)

            hasher.update(
                field.encode()
            )

            hasher.update(
                FingerprintBuilder._serialize(value, visited)
            )

        return hasher.hexdigest()
    
    @staticmethod
    def build(
        operation: Operation
    ) -> str:
        return FingerprintBuilder._build(operation, set())
    


# TODO: Maybe move to another file (?)
class Fingerprintable(
    Protocol
):
    def fingerprint(
        self
    ) -> bytes: ...
    
