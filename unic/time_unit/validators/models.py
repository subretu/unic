from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union, Optional
from unic.time_unit.validators.validators import (
    validate_units,
    validate_timezone,
    validate_unixtime,
    validate_date_formats,
)
from unic.time_unit.constants.constants import (
    VALID_TIME_UNITS,
    VALID_CONVERTED_FORMATS,
    VALID_UNIXTIME_UNITS,
)


class TimeModelValidator(BaseModel):
    data: Union[StrictInt, StrictFloat, list[Union[StrictInt, StrictFloat]]]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_TIME_UNITS, "from_unit")

    @field_validator("to_unit")
    def to_unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_TIME_UNITS, "to_unit")


class DatetimeModelValidator(BaseModel):
    data: Union[StrictInt, list[StrictInt]]
    format: StrictStr
    tz: Optional[StrictStr]

    @field_validator("data")
    def data_check(
        cls, value: Union[StrictInt, list[StrictInt]]
    ) -> Union[float, list[float]]:
        if isinstance(value, list):
            return [validate_unixtime(num) for num in value]
        return validate_unixtime(value)

    @field_validator("format")
    def format_check(cls, value: str) -> str:
        return validate_units(value, VALID_CONVERTED_FORMATS, "format")

    @field_validator("tz")
    def timezone_check(cls, value: Optional[str]) -> Optional[str]:
        return validate_timezone(value)


class UnixtimeModelValidator(BaseModel):
    data: Union[StrictStr, list[StrictStr]]
    tz: Optional[StrictStr]
    unit: Optional[StrictStr]

    @field_validator("data")
    def data_check(
        cls, value: Union[StrictStr, list[StrictStr]]
    ) -> Union[str, list[str]]:
        if isinstance(value, list):
            return [validate_date_formats(datetime_str) for datetime_str in value]
        return validate_date_formats(value)

    @field_validator("tz")
    def timezone_check(cls, value: Optional[str]) -> Optional[str]:
        return validate_timezone(value)

    @field_validator("unit")
    def unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_UNIXTIME_UNITS, "unit")
