from ai_simple_engine.types.data_type.base.base import DataType
from typing import Union
from abc import ABC


class Port(
    ABC
):
    """
    An entry or exit port of a node. A node can
    have 1-n entry ports and 1-n exit port.

    The entry port is an `Input` and the exit port
    is an `Output`.
    """

    def __init__(
        self,
        data_type: DataType,
        *,
        description: str | None = None
    ):
        self.name: Union[str, None] = None
        self.type = data_type
        """
        The engine's type of this port.
        """
        self.description = description

    def __set_name__(
        self,
        owner,
        name
    ):
        self.name = name

    def schema(
        self
    ) -> dict:
        return {
            'name': self.name,
            'type': self.type.schema(),
            'description': self.description
        }