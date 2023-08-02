from pydantic import (
    BaseModel,
    StrictFloat,
    ValidationError,
    field_validator,
    StrictInt,
    StrictStr,
)
from unic.utils import config_parser
from fractions import Fraction
from typing import Union


class TimeUnitModel(BaseModel):
    # 自動変換を防ぐ型で定義
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


class TimeUnit:
    def convert(self, data: int, *, from_unit: str = None, to_unit: str = None) -> int:
        try:
            self.check_parameter_count(from_unit, to_unit)
            input_data = TimeUnitModel(data=data, from_unit=from_unit, to_unit=to_unit)
        except ValidationError as e:
            raise ValueError(e.errors()[0]["msg"])

        parameter = config_parser.parse_toml("unit")
        data = float(input_data.data * Fraction(parameter[from_unit][to_unit]))

        return data

    def check_parameter_count(self, from_unit: str, to_unit: str) -> bool:
        if from_unit is None and to_unit is None:
            raise ValueError("Both 'from_unit' and 'to_unit' arguments are required.")
        elif from_unit is None:
            raise ValueError("The 'from_unit' argument is required.")
        elif to_unit is None:
            raise ValueError("The 'to_unit' argument is required.")
        else:
            return
