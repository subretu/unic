from datetime import timezone, timedelta
from typing import Union


def get_timezone(model_config: dict, tz: Union[str, None] = None) -> timezone:
    return timezone(timedelta(hours=model_config.get(tz, {}).get("value", 0)))


def get_time_unit_conversion_factor(
    model_config: dict, from_unit: str, to_unit: str
) -> Union[str, None]:
    return model_config.get(from_unit, {}).get(to_unit, None)
