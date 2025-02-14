from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union
from unic.length_unit.validators.validators import (
    validate_units,
)


class MetricSystemModelValidator(BaseModel):
    data: Union[StrictInt, StrictFloat, list[Union[StrictInt, StrictFloat]]]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, value: str) -> str:
        return validate_units(value, "from_unit")

    @field_validator("to_unit")
    def to_unit_check(cls, value: str) -> str:
        return validate_units(value, "to_unit")
