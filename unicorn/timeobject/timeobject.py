from datetime import date, datetime, timezone, timedelta
from ..config import settings
from ..utils import check_parameter


class TimeObject:
    def convert_datetime(self, data: int, **kwargs: any) -> datetime:
        try:
            check_parameter.check_number(kwargs)
            check_parameter.check_name(kwargs)
            if len(kwargs) == 1:
                check_parameter.check_value(kwargs["tz"])

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
        except Exception:
            raise

    def convert_date(self, data: int, **kwargs: any) -> date:
        try:
            check_parameter.check_number(kwargs)
            check_parameter.check_name(kwargs)
            if len(kwargs) == 1:
                check_parameter.check_value(kwargs["tz"])

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
        except Exception:
            raise

    def _count_digits(self, data: int) -> int:
        digits = len(str(abs(data)))

        if digits == 10 or digits == 13:
            return digits
        else:
            raise Exception("Unixtime digits is 10 or 13.")
