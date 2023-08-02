from datetime import date, datetime, timezone, timedelta
from unic.utils import check_parameter, config_parser


class TimeObject:
    def convert(self, data: int, **kwargs: any) -> date:
        self.check_parameter_name(kwargs)
        tz = kwargs.get("tz", None)
        target = kwargs["target"]

        if tz:
            check_parameter.check_value(tz)
            parameter = config_parser.parse_toml("timezone")
            timezone_hour = parameter[tz]["value"]
        else:
            timezone_hour = 0

        digits = self.count_digits(data)

        dt_timestamp = self.convert_timestamp_by_digits(data, digits, timezone_hour)

        if target == "datetime":
            return dt_timestamp
        elif target == "date":
            return dt_timestamp.date()
        else:
            raise ValueError("Invalid target")

    def count_digits(self, data: int) -> int:
        digits = len(str(abs(data)))

        if digits == 10 or digits == 13:
            return digits
        else:
            raise ValueError("Unixtime digits is 10 or 13.")

    def convert_timestamp_by_digits(
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

    def check_parameter_name(self, parameter_name: dict) -> None:
        if (len(parameter_name) == 1) and ("target" in parameter_name):
            return
        elif (
            (len(parameter_name) == 2)
            and ("target" in parameter_name)
            and ("tz" in parameter_name)
        ):
            return
        else:
            raise ValueError("Invalid parameter name.")
