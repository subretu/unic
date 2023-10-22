from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from unic.utils import config_parser, validators


class UnixtimeModel:
    def convert(self, data: str, **kwargs: any) -> int:
        self.check_parameter_count(kwargs)

        timezone_hour = 0
        tz = kwargs.get("tz", None)

        try:
            input_data = validators.UnixtimeModelValidator(data=data, tz=tz)
        except ValidationError as e:
            raise ValueError(e.errors()[0]["msg"])

        if len(kwargs) == 1:
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

    def check_parameter_count(self, parameter: dict) -> None:
        if len(parameter) <= 1:
            return
        else:
            raise ValueError(
                "Too many parameter.If specify parameters to the function,the number should be one."
            )
