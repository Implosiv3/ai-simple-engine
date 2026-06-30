from ai_simple_engine.types.validator.abstract import DataTypeValidator
from ai_simple_engine.types.validator.exceptions import ValidationError


class ChoicesDataTypeValidator(
    DataTypeValidator
):

    def __init__(
        self,
        *choices
    ):
        self._choices = set(choices)

    def validate(
        self,
        name: str,
        value
    ) -> None:
        if value not in self._choices:
            raise ValidationError(
                f"'{name}' must be one of {sorted(self._choices)}."
            )
        
    # TODO: Add 'schema'