from .time_unit.time.time_model import TimeModel
from .time_unit.datetime.datetime_model import DatetimeModel
from .time_unit.unixtime.unixtime_model import UnixtimeModel
from .length_unit.metric_system.metric_system_model import MetricSystemModel
from typing import List, Union, Dict, Type

_model_classes: Dict[str, Type] = {
    "time": TimeModel,
    "datetime": DatetimeModel,
    "unixtime": UnixtimeModel,
    "metric_system": MetricSystemModel,
}

_convert_model_instances: Dict[
    str, Union[TimeModel, DatetimeModel, UnixtimeModel, MetricSystemModel]
] = {}


def load_model(
    name: str,
) -> Union[TimeModel, DatetimeModel, UnixtimeModel, MetricSystemModel]:
    if name not in _model_classes:
        raise RuntimeError(
            f"Model {name} not found, available models = {available_models()}"
        )

    if name not in _convert_model_instances:
        _convert_model_instances[name] = _model_classes[name]()

    return _convert_model_instances[name]


def available_models() -> List[str]:
    return list(_model_classes.keys())
