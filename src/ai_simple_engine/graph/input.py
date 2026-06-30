from ai_simple_engine.types.data_type.base import DataType
from ai_simple_engine.types.validator.exceptions import ValidationError
from ai_simple_engine.graph.port_reference import PortReference
from ai_simple_engine.graph.port import Port
from typing import Union


MISSING = object

class Input(
    Port
):
    
    @property
    def has_default(
        self
    ) -> bool:
        return self.default is not MISSING

    def __init__(
        self,
        type: DataType,
        *,
        default = MISSING,
        is_optional: bool = False,
        validators: Union[list['DataTypeValidator'], None] = [],
        description: Union[str, None] = None
    ):
        super().__init__(
            data_type = type,
            description = description
        )

        self.default = default
        self.is_optional = is_optional
        self.validators = validators

        # Previously, due to the '__set_name__'
        # self.name: Union[str, None] = None

    def validate(
        self,
        value
    ):
        if isinstance(value, PortReference):
            return
        
        if value is None:
            if self.optional:
                return

            raise ValidationError(f'"{self.name}" cannot be None.')

        # TODO: Is this ok (?)
        # Validate if non-basic type
        validate_function = getattr(self.type, 'validate', None)
        if callable(validate_function):
            self.type.validate(value)
        
        for validator in self.validators:
            validator.validate(
                self.name,
                value
            )

    def schema(
        self
    ):
        schema = super().schema()

        default_value = (
            None
            if self.default is MISSING else
            self.default
        )

        schema.update({
            'default': default_value,
            'is_optional': self.optional,
            'validators': [
                validator.schema()
                for validator in self.validators
            ]
        })

        return schema

    def __get__(
        self,
        instance,
        owner
    ):
        if instance is None:
            return self

        if self.name in instance._resolved_inputs:
            return instance._resolved_inputs[self.name]

        return instance._connections[self.name]

    