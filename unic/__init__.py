from .time_unit.time.time_model import TimeModel
from .time_unit.datetime.datetime_model import DatetimeModel
from .time_unit.unixtime.unixtime_model import UnixtimeModel
from typing import Union

_convert_model_list = {
    "time": TimeModel(),
    "datetime": DatetimeModel(),
    "unixtime": UnixtimeModel(),
}


def load_model(
    name: str,
) -> Union[TimeModel, DatetimeModel, UnixtimeModel]:
    try:
        convert_model = _convert_model_list[name]
        return convert_model
    except:
        raise ValueError("Invalid model name.")
