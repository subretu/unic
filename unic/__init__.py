from .time_unit.time.time_model import TimeModel
from .time_unit.datetime.datetime_model import DatetimeModel
from .time_unit.unixtime.unixtime_model import UnixtimeModel
from typing import List, Union

_convert_model_list = {
    "time": TimeModel(),
    "datetime": DatetimeModel(),
    "unixtime": UnixtimeModel(),
}


def load_model(
    name: str,
) -> Union[TimeModel, DatetimeModel, UnixtimeModel]:
    if name in _convert_model_list:
        convert_model = _convert_model_list[name]
        return convert_model
    else:
        raise RuntimeError(
            f"Model {name} not found, available models = {available_models()}"
        )


def available_models() -> List[str]:
    return list(_convert_model_list.keys())
