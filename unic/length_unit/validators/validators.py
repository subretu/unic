from unic.length_unit.constants.constants import VALID_METRIC_SYSTEM_UNITS


def validate_units(value: str, parameter: str) -> str:
    if value not in VALID_METRIC_SYSTEM_UNITS:
        raise ValueError(
            f"{value} is invalid value for parameter: {parameter}. Allowed values are {VALID_METRIC_SYSTEM_UNITS}."
        )
    return value
