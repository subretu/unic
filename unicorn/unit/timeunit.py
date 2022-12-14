from pydantic import (
    BaseModel, ValidationError, validator, StrictInt, StrictStr
)


class TimeUnitrModel(BaseModel):
    # 自動変換を防ぐ型で定義
    data: StrictInt
    unit: StrictStr

    @validator("unit")
    def unit_check(cls, v):
        if v not in ["msec", "sec", "min", "hour"]:
            raise ValueError("Undefined unit.")
        return v


def _initial_data(data: int, unit: str):
    try:
        input_data = TimeUnitrModel(data=data, unit=unit)
        return input_data
    except ValidationError as e:
        print(e)
        raise


class TimeUnit:
    def convert_millisecond(self, data: int, unit: str) -> int:
        try:
            input_data = _initial_data(data, unit)
            if input_data.unit == "msec":
                return input_data.data
            elif input_data.unit == "sec":
                return input_data.data * 1000
            elif input_data.unit == "min":
                return input_data.data * 60 * 1000
            elif input_data.unit == "hour":
                return input_data.data * 3600 * 1000
            else:
                raise
        except Exception:
            raise

    def convert_second(self, data: int, unit: str) -> int:
        try:
            input_data = _initial_data(data, unit)
            if input_data.unit == "msec":
                return input_data.data / 1000
            elif input_data.unit == "sec":
                return input_data.data
            elif input_data.unit == "min":
                return input_data.data * 60
            elif input_data.unit == "hour":
                return input_data.data * 3600
            else:
                raise
        except Exception:
            raise

    def convert_minute(self, data: int, unit: str) -> int:
        try:
            input_data = _initial_data(data, unit)
            if input_data.unit == "msec":
                return (input_data.data / 60) / 1000
            elif input_data.unit == "sec":
                return input_data.data / 60
            elif input_data.unit == "min":
                return input_data.data
            elif input_data.unit == "hour":
                return input_data.data * 60
            else:
                raise
        except Exception:
            raise

    def convert_hour(self, data: int, unit: str) -> int:
        try:
            input_data = _initial_data(data, unit)
            if input_data.unit == "msec":
                return (input_data.data / 3600) / 1000
            elif input_data.unit == "sec":
                return input_data.data / 3600
            elif input_data.unit == "min":
                return input_data.data / 60
            elif input_data.unit == "hour":
                return input_data.data
            else:
                raise
        except Exception:
            raise
