from datetime import date, datetime, timezone, timedelta
from ..utils import check_parameter, config_parser


class TimeObject:
    def convert(self, data: int, **kwargs: any) -> date:
        try:
            self._check_parameter_name(kwargs)

            if len(kwargs) == 2:
                check_parameter.check_value(kwargs["tz"])
                parameter = config_parser.parse_toml("./unicorn/configs/timezone.toml")
                timezone_hour = parameter[kwargs["tz"]]["value"]
            else:
                timezone_hour = 0

            digits = self._count_digits(data)

            dt_timestamp = self._convert_timestamp_by_digits(
                data, digits, timezone_hour
            )

            if kwargs["target"] == "datetime":
                return dt_timestamp
            elif kwargs["target"] == "date":
                return dt_timestamp.date()
            else:
                raise
        except Exception:
            raise

    def _count_digits(self, data: int) -> int:
        digits = len(str(abs(data)))

        if digits == 10 or digits == 13:
            return digits
        else:
            raise Exception("Unixtime digits is 10 or 13.")

    def _convert_timestamp_by_digits(
        self, data: int, digits: int, timezone_hour: int
    ) -> datetime:
        if digits == 10:
            dt_timestamp = datetime.fromtimestamp(
                data,
                timezone(timedelta(hours=timezone_hour)),
            )
            return dt_timestamp
        elif digits == 13:
            dt_timestamp = datetime.fromtimestamp(
                data / 1000,
                timezone(timedelta(hours=timezone_hour)),
            )
            return dt_timestamp

    def _check_parameter_name(self, parameter_name: dict) -> None:
        if (len(parameter_name) == 1) and ("target" in parameter_name):
            pass
        elif (
            (len(parameter_name) == 2)
            and ("target" in parameter_name)
            and ("tz" in parameter_name)
        ):
            pass
        else:
            raise Exception("Invalid parameter name.")
