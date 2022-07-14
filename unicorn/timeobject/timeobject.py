from datetime import datetime, timezone, timedelta
from .config import settings


class TimeObject:
    def convert_timestamp(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                if len(str(abs(data))) == 10:
                    dt_timestamp = datetime.fromtimestamp(data, timezone.utc)
                    return dt_timestamp
                elif len(str(abs(data))) == 13:
                    dt_timestamp = datetime.fromtimestamp(data / 1000, timezone.utc)
                    return dt_timestamp
                else:
                    raise ValueError("Unixtime digits is 10 or 13.")
            elif len(kwargs) == 1:
                for key in kwargs.keys():
                    if key == "tz":
                        if len(str(abs(data))) == 10:
                            dt_timestamp = datetime.fromtimestamp(
                                data,
                                timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                            )
                            return dt_timestamp
                        elif len(str(abs(data))) == 13:
                            dt_timestamp = datetime.fromtimestamp(
                                data / 1000,
                                timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                            )
                            return dt_timestamp
                        else:
                            raise Exception(
                                "Unixtime digits is 10 or 13."
                            )
                    else:
                        raise Exception("Parameter name not defined.")
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def convert_unixtime(self, data, **kwargs):
        try:
            except_milisecond = data[0:19]
            milisecond = data[20:23]
            if len(kwargs) == 0:
                dt_timestamp = datetime.strptime(except_milisecond, "%Y-%m-%d %H:%M:%S")
                dt_unixtime = (
                    str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp())) + milisecond
                )
                return dt_unixtime
            elif len(kwargs) == 1:
                for key in kwargs.keys():
                    if key == "tz":
                        dt_timestamp = datetime.strptime(
                            except_milisecond, "%Y-%m-%d %H:%M:%S"
                        ) + timedelta(hours=settings.TIMEZONE[kwargs["tz"]])
                        dt_unixtime = (str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp())) + milisecond
                        )
                        return dt_unixtime
                    else:
                        raise NameError("Parameter name not defined.")
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise
