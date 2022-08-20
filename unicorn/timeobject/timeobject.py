from datetime import datetime, timezone, timedelta
from ..config import settings
from ..utils import check_parameter


class TimeObject:
    def convert_datetime(self, data, **kwargs):
        try:
            if len(kwargs) <= 1:
                check_parameter.check_parameter_name(kwargs)

                if len(kwargs) == 1:
                    check_parameter.check_parameter_value(kwargs["tz"])

                timezone_hour = (
                    lambda: settings.TIMEZONE[kwargs["tz"]] if len(kwargs) == 1 else 0
                )

                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(
                        data,
                        timezone(timedelta(hours=timezone_hour())),
                    )
                    return dt_timestamp
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(
                        data / 1000,
                        timezone(timedelta(hours=timezone_hour())),
                    )
                    return dt_timestamp
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def convert_date(self, data, **kwargs):
        try:
            if len(kwargs) <= 1:
                check_parameter.check_parameter_name(kwargs)

                if len(kwargs) == 1:
                    check_parameter.check_parameter_value(kwargs["tz"])

                timezone_hour = (
                    lambda: settings.TIMEZONE[kwargs["tz"]] if len(kwargs) == 1 else 0
                )

                digits = self._count_digits(data)

                if digits == 10:
                    dt_timestamp = datetime.fromtimestamp(
                        data,
                        timezone(timedelta(hours=timezone_hour())),
                    )
                    return dt_timestamp.date()
                elif digits == 13:
                    dt_timestamp = datetime.fromtimestamp(
                        data / 1000,
                        timezone(timedelta(hours=timezone_hour())),
                    )
                    return dt_timestamp.date()
            else:
                raise Exception("Too many parameter.")
        except Exception:
            raise

    def _count_digits(self, data):
        digits = len(str(abs(data)))

        if digits == 10 or digits == 13:
            return digits
        else:
            raise Exception("Unixtime digits is 10 or 13.")
