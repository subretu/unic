from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union, Optional
from datetime import datetime
from unic.utils import config_parser
from unic.time_unit.constants.constants import (
    VALID_TIME_UNITS,
    VALID_CONVERTED_FORMATS,
    VALID_TIMESTAMP_FORMATS,
    VALID_UNIXTIME_UNITS,
)


class TimezoneConfigCache:
    _timezone_cache: Optional[dict[str, dict[str, float]]] = None

    @classmethod
    def get_valid_timezones(cls) -> dict[str, dict[str, float]]:
        if cls._timezone_cache is None:
            cls._timezone_cache = config_parser.parse_toml("timezone")
        return cls._timezone_cache


def validate_units(value: str, valid_units: list[str], parameter: str) -> str:
    if value not in valid_units:
        raise ValueError(
            f"{value} is invalid value for parameter: {parameter}. Allowed values are {valid_units}."
        )
    return value


def validate_timezone(value: Optional[str]) -> Optional[str]:
    valid_timezones = TimezoneConfigCache.get_valid_timezones()
    if value and value not in valid_timezones:
        raise ValueError(f"{value} is invalid value for parameter: tz.")
    return value


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
        def validate_unixtime(value: int) -> float:
            digits = len(str(abs(value)))
            if digits == 10:
                return float(value)
            elif digits == 13:
                return value / 1000
            else:
                raise ValueError("Unixtime digits is 10 or 13.")

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
        def validate_date_formats(value: str) -> str:
            for date_format in VALID_TIMESTAMP_FORMATS:
                try:
                    datetime.strptime(value, date_format)
                    return value
                except ValueError:
                    continue
            raise ValueError(
                f"'{value}' is invalid date format. Allowed formats are {VALID_TIMESTAMP_FORMATS}."
            )

        if isinstance(value, list):
            return [validate_date_formats(datetime_str) for datetime_str in value]
        return validate_date_formats(value)

    @field_validator("tz")
    def timezone_check(cls, value: Optional[str]) -> Optional[str]:
        return validate_timezone(value)

    @field_validator("unit")
    def unit_check(cls, value: str) -> str:
        return validate_units(value, VALID_UNIXTIME_UNITS, "unit")
