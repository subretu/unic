from pydantic import (
    BaseModel,
    StrictFloat,
    field_validator,
    StrictInt,
    StrictStr,
)
from typing import Union


class TimeModelValidator(BaseModel):
    # Prevent automatic conversion
    data: Union[StrictInt, StrictFloat]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, v):
        valid_units = ["msec", "sec", "min", "hour"]
        if v not in valid_units:
            raise ValueError(
                f"Invalid from_unit name: {v}. Allowed values are {valid_units}."
            )
        return v

    @field_validator("to_unit")
    def to_unit_check(cls, v):
        valid_units = ["msec", "sec", "min", "hour"]
        if v not in valid_units:
            raise ValueError(
                f"Invalid to_unit name: {v}. Allowed values are {valid_units}."
            )
        return v
