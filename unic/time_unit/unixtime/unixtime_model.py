from pydantic import ValidationError
from datetime import datetime, timezone
from unic.utils import config_parser, time_helpers
from unic.time_unit.validators import validators
from unic.time_unit.exceptions.exceptions import UnixtimeValidationError


class UnixtimeModel:
    def __init__(self):
        self.timezone_parameters = config_parser.parse_toml("timezone")

    def _convert_unixtime(self, target_data: str, target_timezone: timezone) -> int:
        date_str = target_data[:19]
        millisecond_str = target_data[20:23]

        dt_with_timezone = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=target_timezone
        )

        dt_timestamp = int(dt_with_timezone.timestamp())
        dt_unixtime = f"{dt_timestamp}{millisecond_str}"

        return int(dt_unixtime)

    def convert(self, data: str, tz: str = None) -> int:
        try:
            input_data = validators.UnixtimeModelValidator(data=data, tz=tz)

            target_timezone = time_helpers.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            return self._convert_unixtime(
                target_data=input_data.data, target_timezone=target_timezone
            )

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise UnixtimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(self, data: list[str], tz: str = None) -> list[int]:
        try:
            input_data = validators.UnixtimeModelValidator(data=data, tz=tz)

            target_timezone = time_helpers.get_timezone(
                timezone_parameters=self.timezone_parameters, tz=tz
            )

            return [
                self._convert_unixtime(
                    target_data=data, target_timezone=target_timezone
                )
                for data in input_data.data
            ]

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise UnixtimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
