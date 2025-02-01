from pydantic import ValidationError
from datetime import date, datetime, timezone
from unic.utils import config_parser, time_helpers
from unic.time_unit.validators import validators
from typing import Union
from unic.time_unit.exceptions.exceptions import DatetimeValidationError


class DatetimeModel:
    def __init__(self):
        self.timezone_parameters = config_parser.parse_toml("timezone")

    def _convert_timestamp(
        self, data: int, target_timezone: timezone, target_format: str
    ) -> Union[date, datetime]:
        timestamp_data = datetime.fromtimestamp(data, target_timezone)

        return timestamp_data if target_format == "datetime" else timestamp_data.date()

    def convert(self, data: int, format: str, tz: str = None) -> Union[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )

            target_timezone = time_helpers.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            return self._convert_timestamp(
                data=input_data.data,
                target_timezone=target_timezone,
                target_format=format,
            )

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[int], format: str, tz: str = None
    ) -> list[Union[date, datetime]]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )

            target_timezone = time_helpers.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            return [
                self._convert_timestamp(
                    data=data,
                    target_timezone=target_timezone,
                    target_format=format,
                )
                for data in input_data.data
            ]

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
