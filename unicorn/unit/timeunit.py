from pydantic import BaseModel, ValidationError, validator, StrictInt, StrictStr
import toml


class TimeUnitrModel(BaseModel):
    # 自動変換を防ぐ型で定義
    data: StrictInt
    unit: StrictStr

    @validator("unit")
    def unit_check(cls, v):
        if v not in ["msec", "sec", "min", "hour"]:
            raise ValueError("Undefined unit.")
        return v


def parse_setting():
    with open("./unicorn/unit/config/unit_settings.toml") as f:
        obj = toml.load(f)
        return obj


def _initial_data(data: int, unit: str):
    try:
        input_data = TimeUnitrModel(data=data, unit=unit)
        return input_data
    except ValidationError as e:
        print(e)
        raise


class TimeUnit:
    def convert(self, data: int, from_unit: str, to_unit: str) -> int:
        try:
            input_data = _initial_data(data, to_unit)
            parameter = parse_setting()
            data = input_data.data * parameter[from_unit][to_unit]
            return data
        except Exception:
            raise
