from typing import Optional
from datetime import datetime
from unic.utils import config_parser
from unic.time_unit.constants.constants import (
    VALID_TIMESTAMP_FORMATS,
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


def validate_unixtime(value: int) -> float:
    digits = len(str(abs(value)))
    if digits == 10:
        return float(value)
    elif digits == 13:
        return value / 1000
    else:
        raise ValueError("Unixtime digits is 10 or 13.")


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
