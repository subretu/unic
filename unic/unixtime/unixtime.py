from datetime import datetime, timezone, timedelta
from unic.utils import check_parameter, config_parser


class Unixtime:
    def convert(self, data: str, **kwargs: any) -> int:
        check_parameter.check_number(kwargs)

        if len(kwargs) == 1:
            tz = kwargs.get("tz", None)
            check_parameter.check_value(tz)
            parameter = config_parser.parse_toml("timezone")
            timezone_hour = parameter[tz]["value"]
        else:
            timezone_hour = 0

        except_milisecond = data[0:19]
        milisecond = data[20:23]

        dt_timestamp = datetime.strptime(
            except_milisecond, "%Y-%m-%d %H:%M:%S"
        ) + timedelta(hours=timezone_hour)

        dt_unixtime = (
            str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))
        ) + milisecond

        return int(dt_unixtime)
