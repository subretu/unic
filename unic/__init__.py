from importlib import import_module
from typing import List, Dict, Any

# Mapping of model name -> (module_path, class_name). Models are imported lazily.
_model_paths: Dict[str, tuple] = {
    "time": ("unic.time_unit.time.time_model", "TimeModel"),
    "datetime": ("unic.time_unit.datetime.datetime_model", "DatetimeModel"),
    "unixtime": ("unic.time_unit.unixtime.unixtime_model", "UnixtimeModel"),
}

_convert_model_instances: Dict[str, Any] = {}


def load_model(name: str) -> Any:
    if name not in _model_paths:
        raise RuntimeError(
            f"Model {name} not found, available models = {available_models()}"
        )

    if name not in _convert_model_instances:
        module_name, class_name = _model_paths[name]
        module = import_module(module_name)
        cls = getattr(module, class_name)
        _convert_model_instances[name] = cls()

    return _convert_model_instances[name]


def available_models() -> List[str]:
    return list(_model_paths.keys())


__all__ = ["load_model", "available_models"]
