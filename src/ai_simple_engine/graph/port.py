from ai_simple_engine.types.data_type import DataType
from dataclasses import dataclass
from typing import Union


@dataclass(slots = True)
class Port:
    """
    An entry or exit port of a node. A node can
    have 1-n entry ports and 1-n exit port.

    The entry port is an `Input` and the exit port
    is an `Output`.
    """

    name: Union[str, None] = None
    type: DataType