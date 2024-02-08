from pydantic import BaseModel, StrictFloat, field_validator, StrictInt, StrictStr
from typing import Union
from datetime import datetime
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


class TimeModelValidator(BaseModel, ValidatorMixin):
    data: Union[StrictInt, StrictFloat]
    from_unit: StrictStr
    to_unit: StrictStr

    @field_validator("from_unit")
    def from_unit_check(cls, v):
        return cls.validate_units(v, ["msec", "sec", "min", "hour"], "from_unit")

    @field_validator("to_unit")
    def to_unit_check(cls, v):
        return cls.validate_units(v, ["msec", "sec", "min", "hour"], "to_unit")


class DatetimeModelValidator(BaseModel, ValidatorMixin):
    data: StrictInt
    format: StrictStr
    tz: Union[StrictStr, None]

    @field_validator("data")
    def data_check(cls, v):
        digits = len(str(abs(v)))
        if digits == 10 or digits == 13:
            return v
        else:
            raise ValueError("Unixtime digits is 10 or 13.")

    @field_validator("format")
    def format_check(cls, v):
        return cls.validate_units(v, ["datetime", "date"], "format")

    @field_validator("tz")
    def timezone_check(cls, v):
        return cls.validate_timezone(v)


class UnixtimeModelValidator(BaseModel, ValidatorMixin):
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
        return cls.validate_timezone(v)


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
