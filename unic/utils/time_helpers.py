from datetime import timezone, timedelta
from typing import Union


def get_timezone(timezone_parameters: dict, tz: Union[str, None] = None) -> timezone:
    timezone_hour = timezone_parameters.get(tz, {}).get("value", 0)

    return timezone(timedelta(hours=timezone_hour))
