import datetime
from .config import settings


class ConvertDateTime:
    def convert_timestamp(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                dt = datetime.datetime.fromtimestamp(data, datetime.timezone.utc)
                return dt.strftime("%Y-%m-%d %H:%M:%S")
            elif len(kwargs) == 1:
                for key in kwargs.keys():
                    if key == "tz":
                        dt = datetime.datetime.fromtimestamp(
                            data, datetime.timezone(datetime.timedelta(hours=settings.TIMEZONE["Asia/Tokyo"]))
                        )
                        return dt.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        raise Exception("Parameter name error.")
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise
