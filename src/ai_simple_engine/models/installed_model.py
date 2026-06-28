from ai_simple_engine.models.model_spec import ModelSpec
from ai_simple_engine.models.model_family import ModelFamily
from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass(frozen = True)
class InstalledModel:

    spec: ModelSpec
    path: Path

    @property
    def family(
        self
    ) -> ModelFamily:
        """
        Get the `family` of the specifications `spec`.
        """
        return self.spec.family
    
    @property
    def provider(
        self
    ) -> ModelFamily:
        """
        Get the `provider` of the specifications `spec`.
        """
        return self.spec.provider
    
    @property
    def identifier(
        self
    ) -> str:
        """
        Get the `identifier` of the specifications `spec`.
        """
        return self.spec.identifier
    
    @property
    def revision(
        self
    ) -> Union[str, None]:
        """
        Get the `revision` of the specifications `spec`.
        """
        return self.spec.revision