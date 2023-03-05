from datetime import datetime, timezone, timedelta
from ..utils import check_parameter, config_parser


class Unixtime:
    def convert(self, data: str, **kwargs: any) -> int:
        try:
            except_milisecond = data[0:19]
            milisecond = data[20:23]

            check_parameter.check_number(kwargs)

            if len(kwargs) == 1:
                check_parameter.check_name(kwargs)
                parameter = config_parser.parse_toml("./unicorn/configs/timezone.toml")
                timezone_hour = parameter[kwargs["tz"]]["value"]
            else:
                timezone_hour = 0

            dt_timestamp = datetime.strptime(
                except_milisecond, "%Y-%m-%d %H:%M:%S"
            ) + timedelta(hours=timezone_hour)

            dt_unixtime = (
                str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))
            ) + milisecond

            return int(dt_unixtime)
        except Exception:
            raise
