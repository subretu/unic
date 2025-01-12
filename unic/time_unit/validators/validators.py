from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union, Optional
from datetime import datetime
from unic.utils import config_parser


class TimezoneConfigCache:
    _timezone_cache: Optional[dict[str, str]] = None

    @classmethod
    def get_valid_timezones(cls) -> dict[str, str]:
        if cls._timezone_cache is None:
            cls._timezone_cache = config_parser.parse_toml("timezone")
        return cls._timezone_cache


class ValidatorMixin:
    @classmethod
    def validate_units(cls, v: str, valid_units: list[str], parameter: str) -> str:
        if v not in valid_units:
            raise ValueError(
                f"{v} is invalid value for parameter: {parameter}. Allowed values are {valid_units}."
            )
        return v

    @classmethod
    def validate_timezone(cls, v: Optional[str]) -> Optional[str]:
        valid_timezones = TimezoneConfigCache.get_valid_timezones()
        if v not in valid_timezones.keys() and v is not None:
            raise ValueError(f"{v} is invalid value for parameter: tz.")
        return v


class TimeModelValidator(BaseModel, ValidatorMixin):
    data: Union[StrictInt, StrictFloat, list[Union[StrictInt, StrictFloat]]]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, v: str) -> str:
        return cls.validate_units(v, ["msec", "sec", "min", "hour"], "from_unit")

    @field_validator("to_unit")
    def to_unit_check(cls, v: str) -> str:
        return cls.validate_units(v, ["msec", "sec", "min", "hour"], "to_unit")


class DatetimeModelValidator(BaseModel, ValidatorMixin):
    data: Union[StrictInt, list[StrictInt]]
    format: StrictStr
    tz: Optional[StrictStr]

    @field_validator("data")
    def data_check(
        cls, v: Union[StrictInt, list[StrictInt]]
    ) -> Union[float, list[float]]:
        def validate_unixtime(value: int) -> float:
            digits = len(str(abs(value)))
            if digits == 10:
                return float(value)
            elif digits == 13:
                return value / 1000
            else:
                raise ValueError("Unixtime digits is 10 or 13.")

        if isinstance(v, list):
            return [validate_unixtime(value) for value in v]
        return validate_unixtime(v)

    @field_validator("format")
    def format_check(cls, v: str) -> str:
        return cls.validate_units(v, ["datetime", "date"], "format")

    @field_validator("tz")
    def timezone_check(cls, v: Optional[str]) -> Optional[str]:
        return cls.validate_timezone(v)


class UnixtimeModelValidator(BaseModel, ValidatorMixin):
    data: Union[StrictStr, list[StrictStr]]
    tz: Optional[StrictStr]

    @field_validator("data")
    def data_check(cls, v: Union[StrictStr, list[StrictStr]]) -> Union[str, list[str]]:
        def validate_date_formats(value: str) -> str:
            date_formats = [
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%d %H:%M:%S.%f",
                "%Y/%m/%d %H:%M:%S",
                "%Y/%m/%d %H:%M:%S.%f",
            ]
            for date_format in date_formats:
                try:
                    datetime.strptime(value, date_format)
                    return value
                except ValueError:
                    continue
            raise ValueError(
                f"'{value}' is invalid date format. Allowed formats are {date_formats}."
            )

        if isinstance(v, list):
            return [validate_date_formats(value) for value in v]
        return validate_date_formats(v)

    @field_validator("tz")
    def timezone_check(cls, v: Optional[str]) -> Optional[str]:
        return cls.validate_timezone(v)
