from ai_simple_engine.types.validator.abstract import DataTypeValidator
from ai_simple_engine.types.validator.exceptions import ValidationError


class LengthDataTypeValidator(
    DataTypeValidator
):

    def __init__(
        self,
        minimum = None,
        maximum = None
    ):
        self.minimum = minimum
        self.maximum = maximum

    def validate(
        self,
        name: str,
        value
    ) -> None:

        length = len(value)

        if (
            self.minimum is not None and
            length < self.minimum
        ):
            raise ValidationError(
                f'"{name}" must contain at least {self.minimum} elements.'
            )

        if (
            self.maximum is not None and
            length > self.maximum
        ):
            raise ValidationError(
                f'"{name}" must contain at most {self.maximum} elements.'
            )
        
    # TODO: Add 'schema'