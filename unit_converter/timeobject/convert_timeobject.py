import datetime
import time
from .config import settings


class ConvertTimeObject:
    def convert_timestamp(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                if len(str(abs(data))) == 10:
                    dt_timestamp = datetime.datetime.fromtimestamp(data, datetime.timezone.utc)
                    return dt_timestamp
                elif len(str(abs(data))) == 13:
                    dt_timestamp = datetime.datetime.fromtimestamp(
                        data / 1000, datetime.timezone.utc
                    )
                    return dt_timestamp
                else:
                    raise Exception("Unixtime digits error.")
            elif len(kwargs) == 1:
                for key in kwargs.keys():
                    if key == "tz" and len(str(abs(data))) == 10:
                        dt_timestamp = datetime.datetime.fromtimestamp(
                            data,
                            datetime.timezone(
                                datetime.timedelta(
                                    hours=settings.TIMEZONE[kwargs["tz"]]
                                )
                            ),
                        )
                        return dt_timestamp
                    elif key == "tz" and len(str(abs(data))) == 13:
                        dt_timestamp = datetime.datetime.fromtimestamp(
                            data / 1000,
                            datetime.timezone(
                                datetime.timedelta(
                                    hours=settings.TIMEZONE[kwargs["tz"]]
                                )
                            ),
                        )
                        return dt_timestamp
                    else:
                        raise Exception(
                            "Parameter name error or Unixtime digits error."
                        )
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def convert_unixtime(self, data, **kwargs):
        except_milisecond = data[0:19]
        milisecond = data[20:23]
        dt = datetime.datetime.strptime(except_milisecond, "%Y-%m-%d %H:%M:%S")
        dt_timestamp = datetime.datetime(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second,
        )
        dt_unixtime = str(int(time.mktime(dt_timestamp.timetuple()))) + milisecond
        return dt_unixtime
