from datetime import timezone, timedelta


def get_timezone(timezone_parameters: dict, tz: str = None) -> timezone:
    timezone_hour = timezone_parameters.get(tz, {}).get("value", 0)

    return timezone(timedelta(hours=timezone_hour))
