from datetime import datetime, timezone, timedelta
from ..config import settings
from ..utils import check_parameter


class Unixtime:
    def convert_unixtime(self, data: str, **kwargs: any) -> int:
        try:
            except_milisecond = data[0:19]
            milisecond = data[20:23]

            if len(kwargs) <= 1:
                check_parameter.check_name(kwargs)

                timezone_hour = (
                    lambda: settings.TIMEZONE[kwargs["tz"]] if len(kwargs) == 1 else 0
                )

                dt_timestamp = datetime.strptime(
                    except_milisecond, "%Y-%m-%d %H:%M:%S"
                ) + timedelta(hours=timezone_hour())
                dt_unixtime = (
                    str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))
                ) + milisecond
                return int(dt_unixtime)
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise
