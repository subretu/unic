from datetime import datetime, timezone, timedelta
from ..config import settings


class TimeObject:
    def convert_datetime(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(data, timezone.utc)
                    return dt_timestamp
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(data / 1000, timezone.utc)
                    return dt_timestamp
            elif len(kwargs) == 1:
                self._check_parameter(kwargs)

                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(
                        data,
                        timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                    )
                    return dt_timestamp
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(
                        data / 1000,
                        timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                    )
                    return dt_timestamp
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def convert_date(self, data, **kwargs):
        try:
            if len(kwargs) == 0:
                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(data, timezone.utc)
                    return dt_timestamp.date()
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(data / 1000, timezone.utc)
                    return dt_timestamp.date()
            elif len(kwargs) == 1:
                self._check_parameter(kwargs)

                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(
                        data,
                        timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                    )
                    return dt_timestamp.date()
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(
                        data / 1000,
                        timezone(timedelta(hours=settings.TIMEZONE[kwargs["tz"]])),
                    )
                    return dt_timestamp.date()
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
                return int(dt_unixtime)
            elif len(kwargs) == 1:
                self._check_parameter(kwargs)

                dt_timestamp = datetime.strptime(
                    except_milisecond, "%Y-%m-%d %H:%M:%S"
                ) + timedelta(hours=settings.TIMEZONE[kwargs["tz"]])
                dt_unixtime = (str(int(dt_timestamp.replace(tzinfo=timezone.utc).timestamp()))) + milisecond
                return int(dt_unixtime)
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def _check_parameter(self, params):
        if 'tz' in params:
            pass
        else:
            raise Exception("Parameter name not defined.")

    def _count_digits(self, data):
        digits = len(str(abs(data)))

        if digits == 10 or digits == 13:
            return digits
        else:
            raise Exception("Unixtime digits is 10 or 13.")
