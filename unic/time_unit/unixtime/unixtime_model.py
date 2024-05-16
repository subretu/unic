from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from unic.utils import config_parser
from unic.time_unit.validators import validators


class UnixtimeModel:
    def __init__(self):
        self.timezone_parameters = config_parser.parse_toml("timezone")

    def convert(self, data: str, tz: str = None) -> int:
        try:
            input_data = validators.UnixtimeModelValidator(data=data, tz=tz)
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        timezone_hour = self.timezone_parameters.get(tz, {}).get("value", 0)

        except_milisecond = input_data.data[0:19]
        milisecond = input_data.data[20:23]

        dt_timestamp = datetime.strptime(
            except_milisecond, "%Y-%m-%d %H:%M:%S"
        ) + timedelta(hours=timezone_hour)

        dt_unixtime = (
            str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))
        ) + milisecond

        return int(dt_unixtime)
