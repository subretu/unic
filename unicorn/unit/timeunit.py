from pydantic import BaseModel, ValidationError, validator, StrictInt, StrictStr
from ..utils import config_parser
import os


class TimeUnitModel(BaseModel):
    # 自動変換を防ぐ型で定義
    data: StrictInt
    from_unit: StrictStr
    to_unit: StrictStr

    @validator("from_unit")
    def from_unit_check(cls, v):
        valid_units = ["msec", "sec", "min", "hour"]
        if v not in valid_units:
            raise ValueError(
                f"Invalid from_unit name: {v}. Allowed values are {valid_units}."
            )
        return v

    @validator("to_unit")
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
            input_data = TimeUnitModel(data=data, from_unit=from_unit, to_unit=to_unit)
        except ValidationError as e:
            raise ValueError(str(e))

        config_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "configs",
            "unit",
            "settings.toml",
        )
        parameter = config_parser.parse_toml(config_file_path)
        data = input_data.data * parameter[from_unit][to_unit]

        return data
