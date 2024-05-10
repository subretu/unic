from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from unic.utils import config_parser
from unic.time_unit.validators import validators


class UnixtimeModel:
    def convert(self, data: str, tz: str = None) -> int:
        try:
            input_data = validators.UnixtimeModelValidator(data=data, tz=tz)
        except ValidationError as e:
            raise ValueError(e.errors()[0]["msg"])

        timezone_hour = 0
        if tz:
            parameter = config_parser.parse_toml("timezone")
            timezone_hour = parameter[tz]["value"]

        except_milisecond = input_data.data[0:19]
        milisecond = input_data.data[20:23]

        dt_timestamp = datetime.strptime(
            except_milisecond, "%Y-%m-%d %H:%M:%S"
        ) + timedelta(hours=timezone_hour)

        dt_unixtime = (
            str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))
        ) + milisecond

        return int(dt_unixtime)
