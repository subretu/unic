from pydantic import ValidationError
from datetime import date, datetime, timezone
from unic.utils import config_parser, utils
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

        result = (
            timestamp_data if target_format == "datetime" else timestamp_data.date()
        )

        return result

    def convert(self, data: int, format: str, tz: str = None) -> Union[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )

            target_timezone = utils.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            converted_data = self._convert_timestamp(
                input_data.data, target_timezone, format
            )

            return converted_data

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[int], format: str, tz: str = None
    ) -> list[date, datetime]:
        try:
            input_data = validators.DatetimeModelValidator(
                data=data, format=format, tz=tz
            )

            target_timezone = utils.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            converted_data_list = [
                self._convert_timestamp(data, target_timezone, format)
                for data in input_data.data
            ]

            return converted_data_list

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise DatetimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
