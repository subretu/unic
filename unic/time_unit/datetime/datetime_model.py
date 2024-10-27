from pydantic import ValidationError
from datetime import date, datetime, timezone, timedelta
from unic.utils import config_parser
from unic.time_unit.validators import validators
from typing import Union
from unic.time_unit.exceptions.exceptions import DatetimeValidationError


class DatetimeModel:
    def __init__(self):
        self.timezone_parameters = config_parser.parse_toml("timezone")

    def convert(self, data: int, format: str, tz: str = None) -> Union[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        timezone_hour = self.timezone_parameters.get(tz, {}).get("value", 0)

        converted_data = self.convert_timestamp_by_digits(
            input_data.data, timezone_hour, format
        )

        return converted_data

    def convert_batch(
        self, data: list[int], format: str, tz: str = None
    ) -> list[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )

            timezone_hour = self.timezone_parameters.get(tz, {}).get("value", 0)

            converted_data_list = [
                self.convert_timestamp_by_digits(data, timezone_hour, format)
                for data in input_data.data
            ]

            return converted_data_list

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

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
