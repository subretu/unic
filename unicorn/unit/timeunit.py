from pydantic import BaseModel, ValidationError, validator


class TimeUnitrModel(BaseModel):
    data: int
    unit: str

    @validator("unit")
    def unit_check(cls, v):
        if v not in ["msec", "sec", "min", "hour"]:
            raise ValueError("Undefined unit")
        return v.title()


def _init(data: int, unit: str):
    try:
        input_data = TimeUnitrModel(data=data, unit=unit)
        return input_data
    except ValidationError as e:
        print(e)


class TimeUnit:
    def convert_millisecond(self, data: int, unit: str) -> int:
        try:
            input_data = _init(data, unit)
            if unit == "msec":
                return data
            elif unit == "sec":
                return data * 1000
            elif unit == "min":
                return data * 60 * 1000
            elif unit == "hour":
                return data * 3600 * 1000
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_second(self, data: int, unit: str) -> int:
        try:
            if unit == "msec":
                return data / 1000
            elif unit == "sec":
                return data
            elif unit == "min":
                return data * 60
            elif unit == "hour":
                return data * 3600
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_minute(self, data: int, unit: str) -> int:
        try:
            if unit == "msec":
                return (data / 60) / 1000
            elif unit == "sec":
                return data / 60
            elif unit == "min":
                return data
            elif unit == "hour":
                return data * 60
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_hour(self, data: int, unit: str) -> int:
        try:
            if unit == "msec":
                return (data / 3600) / 1000
            elif unit == "sec":
                return data / 3600
            elif unit == "min":
                return data / 60
            elif unit == "hour":
                return data
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise
