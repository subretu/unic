from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union
from unic.utils import config_parser


class ValidatorMixin:
    @classmethod
    def validate_units(cls, v, valid_units, parameter):
        if v not in valid_units:
            raise ValueError(
                f"{v} is invalid value for parameter: {parameter}. Allowed values are {valid_units}."
            )
        return v

    @classmethod
    def validate_timezone(cls, v):
        valid_timezones = config_parser.parse_toml("timezone")
        if v not in valid_timezones.keys() and v is not None:
            raise ValueError(f"{v} is invalid value for parameter: tz.")
        return v


class MetricSystemModelValidator(BaseModel, ValidatorMixin):
    data: Union[StrictInt, StrictFloat]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, v):
        return cls.validate_units(
            v, ["nm", "um", "mm", "cm", "m", "km", "Mm", "Gm", "Tm"], "from_unit"
        )

    @field_validator("to_unit")
    def to_unit_check(cls, v):
        return cls.validate_units(
            v, ["nm", "um", "mm", "cm", "m", "km", "Mm", "Gm", "Tm"], "to_unit"
        )
