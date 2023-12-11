from pydantic import (
    BaseModel,
    StrictFloat,
    field_validator,
    StrictInt,
    StrictStr,
)
from typing import Union
from datetime import datetime
from unic.utils import config_parser


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
                f"{v} is invalid value for parameter: from_unit. Allowed values are {valid_units}."
            )
        return v

    @field_validator("to_unit")
    def to_unit_check(cls, v):
        valid_units = ["msec", "sec", "min", "hour"]
        if v not in valid_units:
            raise ValueError(
                f"{v} is invalid value for parameter: to_unit. Allowed values are {valid_units}."
            )
        return v


class DatetimeModelValidator(BaseModel):
    # Prevent automatic conversion
    data: StrictInt
    target: StrictStr
    tz: Union[StrictStr, None]

    @field_validator("data")
    def data_check(cls, v):
        digits = len(str(abs(v)))

        if digits == 10 or digits == 13:
            return v
        else:
            raise ValueError("Unixtime digits is 10 or 13.")

    @field_validator("target")
    def target_check(cls, v):
        valid_targets = ["datetime", "date"]
        if v not in valid_targets:
            raise ValueError(
                f"{v} is invalid value for parameter: target. Allowed values are {valid_targets}."
            )
        return v

    @field_validator("tz")
    def timezone_check(cls, v):
        valid_timezones = config_parser.parse_toml("timezone")
        if v not in valid_timezones.keys() and v is not None:
            raise ValueError(f"{v} is invalid value for parameter: tz.")
        return v


class UnixtimeModelValidator(BaseModel):
    # Prevent automatic conversion
    data: StrictStr
    tz: Union[StrictStr, None]

    @field_validator("data")
    def data_check(cls, v):
        date_formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f"]
        for date_format in date_formats:
            try:
                datetime.strptime(v, date_format)
                return v
            except ValueError:
                continue
        raise ValueError(
            f"'{v}' is invalid date format. Allowed formats are {date_formats}."
        )

    @field_validator("tz")
    def timezone_check(cls, v):
        valid_timezones = config_parser.parse_toml("timezone")
        if v not in valid_timezones.keys() and v is not None:
            raise ValueError(f"{v} is invalid value for parameter: tz.")
        return v


class MetricSystemModelValidator(BaseModel):
    # Prevent automatic conversion
    data: Union[StrictInt, StrictFloat]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, v):
        valid_units = ["nm", "um", "mm", "cm", "m", "km", "Mm", "Gm", "Tm"]
        if v not in valid_units:
            raise ValueError(
                f"{v} is invalid value for parameter: from_unit. Allowed values are {valid_units}."
            )
        return v

    @field_validator("to_unit")
    def to_unit_check(cls, v):
        valid_units = ["nm", "um", "mm", "cm", "m", "km", "Mm", "Gm", "Tm"]
        if v not in valid_units:
            raise ValueError(
                f"{v} is invalid value for parameter: to_unit. Allowed values are {valid_units}."
            )
        return v
