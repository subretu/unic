from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union
from unic.length_unit.constants.constants import VALID_METRIC_SYSTEM_UNITS


def validate_units(value: str, valid_units: list[str], parameter: str) -> str:
    if value not in valid_units:
        raise ValueError(
            f"{value} is invalid value for parameter: {parameter}. Allowed values are {valid_units}."
        )
    return value


class MetricSystemModelValidator(BaseModel):
    data: Union[StrictInt, StrictFloat, list[Union[StrictInt, StrictFloat]]]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_METRIC_SYSTEM_UNITS, "from_unit")

    @field_validator("to_unit")
    def to_unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_METRIC_SYSTEM_UNITS, "to_unit")
