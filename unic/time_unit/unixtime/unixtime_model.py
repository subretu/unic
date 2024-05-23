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

        year = int(input_data.data[:4])
        month = int(input_data.data[5:7])
        day = int(input_data.data[8:10])
        hour = int(input_data.data[11:13])
        minute = int(input_data.data[14:16])
        second = int(input_data.data[17:19])
        milisecond = input_data.data[20:23]

        dt_timestamp = (
            datetime(year, month, day, hour, minute, second)
            .replace(tzinfo=timezone.utc)
            .timestamp()
            + timezone_hour * 3600
        )

        dt_unixtime = str(int(dt_timestamp)) + milisecond

        return int(dt_unixtime)
