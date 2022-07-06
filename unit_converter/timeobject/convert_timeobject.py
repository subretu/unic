import datetime
from .config import settings


class ConvertTimeObject:
    def convert_timestamp(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                if len(str(abs(data))) == 10:
                    dt = datetime.datetime.fromtimestamp(data, datetime.timezone.utc)
                    return dt.strftime("%Y-%m-%d %H:%M:%S.%f")
                elif len(str(abs(data))) == 13:
                    dt = datetime.datetime.fromtimestamp( data / 1000, datetime.timezone.utc)
                    return dt.strftime("%Y-%m-%d %H:%M:%S.%f")
                else:
                    raise Exception("Unixtime digits error.")
            elif len(kwargs) == 1:
                for key in kwargs.keys():
                    if key == "tz" and len(str(abs(data))) == 10:
                        dt = datetime.datetime.fromtimestamp(
                            data,
                            datetime.timezone(datetime.timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                        )
                        return dt.strftime("%Y-%m-%d %H:%M:%S")
                    elif key == "tz" and len(str(abs(data))) == 13:
                        dt = datetime.datetime.fromtimestamp(
                            data / 1000,
                            datetime.timezone(datetime.timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                        )
                        return dt.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        raise Exception(
                            "Parameter name error or Unixtime digits error."
                        )
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise
