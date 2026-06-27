from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass(frozen = True)
class InstalledModel:

    id: str
    path: Path
    revision: Union[str, None] = None