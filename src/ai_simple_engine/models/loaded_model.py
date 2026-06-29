from ai_simple_engine.models.installed_model import InstalledModel
from ai_simple_engine.models.model_family import ModelFamily
from dataclasses import dataclass
from typing import Generic, TypeVar, Union


T = TypeVar('T')

@dataclass(frozen = True)
class LoadedModel(
    Generic[T]
):
    """
    A loaded model class including the model that is
    installed and the instance.
    """

    installed_model: InstalledModel
    instance: T

    @property
    def family(
        self
    ) -> ModelFamily:
        """
        Get the `family` of the specifications `spec`
        of the `installed_model`.
        """
        return self.installed_model.family
    
    @property
    def provider(
        self
    ) -> str:
        """
        Get the `provider` of the specifications `spec`
        of the `installed_model`.
        """
        return self.installed_model.provider
    
    @property
    def identifier(
        self
    ) -> str:
        """
        Get the `identifier` of the specifications `spec`
        of the `installed_model`.
        """
        return self.installed_model.identifier
    
    @property
    def revision(
        self
    ) -> Union[str, None]:
        """
        Get the `revision` of the specifications `spec`
        of the `installed_model`.
        """
        return self.installed_model.revision