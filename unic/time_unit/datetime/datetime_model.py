from pydantic import ValidationError
from datetime import date, datetime, timezone, timedelta
from unic.utils import config_parser
from unic.time_unit.validators import validators
from typing import Union
import math


class DatetimeModel:
    def convert(self, data: int, format: str, tz: str = None) -> Union[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )
        except ValidationError as e:
            raise ValueError(e.errors()[0]["msg"])

        timezone_hour = 0
        if tz:
            parameter = config_parser.parse_toml("timezone")
            timezone_hour = parameter[tz]["value"]

        converted_data = self.convert_timestamp_by_digits(
            input_data.data, timezone_hour, format
        )

        return converted_data

    def convert_timestamp_by_digits(
        self, data: int, timezone_hour: int, target_format: str
    ) -> Union[date, datetime]:
        timestamp_data = datetime.fromtimestamp(
            data,
            timezone(timedelta(hours=timezone_hour)),
        )

        result = (
            timestamp_data if target_format == "datetime" else timestamp_data.date()
        )

        return result
