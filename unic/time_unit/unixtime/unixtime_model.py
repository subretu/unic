from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from unic.utils import config_parser, utils
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

        target_timezone = utils.get_timezone(
            timezone_parameters=self.timezone_parameters, tz=tz
        )

        date_str = input_data.data[:19]
        millisecond_str = input_data.data[20:23]

        dt_with_timezone = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=target_timezone
        )

        dt_timestamp = int(dt_with_timezone.timestamp())
        dt_unixtime = f"{dt_timestamp}{millisecond_str}"

        return int(dt_unixtime)
