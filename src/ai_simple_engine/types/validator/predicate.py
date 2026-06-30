from ai_simple_engine.types.validator.abstract import DataTypeValidator
from ai_simple_engine.types.validator.exceptions import ValidationError
from collections.abc import Callable


class PredicateDataTypeValidator(
    DataTypeValidator
):
    """
    Example of this validator:
    ```
    PredicateValidator(
        lambda x: x % 2 == 0,
        '"{name}" must be even.'
    )
    ```
    """

    def __init__(
        self,
        predicate: Callable[[object], bool],
        message: str
    ):
        self._predicate = predicate
        self._message = message

    def validate(
        self,
        name: str,
        value
    ) -> None:
        if not self._predicate(value):
            raise ValidationError(
                self._message.format(
                    name = name,
                    value = value
                )
            )
        
    # TODO: Add 'schema'