from dataclasses import dataclass
from typing import Union, Dict, Optional, Callable
from pathlib import Path


@dataclass(frozen = True)
class ModelSpec:
    """
    A model specification to indicate the model we
    want to obtain and from which source, including
    the next fields:
    - `family`
    - `provider`
    - `identifier`
    - `revision`
    """

    family: str
    provider: str
    """
    Hugginface, a local path, an url. The source of
    the model where we can obtain it.
    """
    identifier: str
    revision: Union[str, None] = None


# TODO: This below is not being used (!)

class ModelRegistry:

    def __init__(
        self
    ):
        self._models: Dict[str, ModelSpec] = {}

    def register(
        self,
        spec: ModelSpec
    ):
        self._models[spec.model_id] = spec

    def get(
        self,
        model_id: str
    ) -> ModelSpec:
        return self._models[model_id]


class ModelStore:

    def __init__(
        self,
        root: str = '~/.cache/ai_engine/models'
    ):
        self.root = Path(root).expanduser()
        self.root.mkdir(parents = True, exist_ok = True)

    def get_model_path(
        self,
        model_id: str,
        revision: str = 'default'
    ) -> Path:
        path = self.root / model_id / revision
        path.mkdir(parents = True, exist_ok = True)

        return path


class ModelDownloader:
    
    def __init__(
        self,
        store: ModelStore
    ):
        self.store = store

    def download(
        self,
        spec: ModelSpec,
        progress: Optional[Callable[[float], None]] = None
    ) -> Path:
        target_dir = self.store.get_model_path(spec.model_id, spec.revision or "default")

        # Logic placeholder
        if progress:
            progress(0.0)

        # TODO: Implement the way to download it
        # self._download_from_source(...)

        if progress:
            progress(1.0)

        return target_dir