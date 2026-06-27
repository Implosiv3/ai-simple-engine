from ai_simple_engine.types.validator.abstract import DataTypeValidator
from ai_simple_engine.types.validator.exceptions import ValidationError


class RangeDataTypeValidator(
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
        if (
            self.minimum is not None and
            value < self.minimum
        ):
            raise ValidationError(
                f'"{name}" must be >= {self.minimum}.'
            )

        if (
            self.maximum is not None and
            value > self.maximum
        ):
            raise ValidationError(
                f'"{name}" must be <= {self.maximum}.'
            )
        
    def schema(
        self
    ):
        return {
            'type': 'range',
            'minimum': self.minimum,
            'maximum': self.maximum
        }