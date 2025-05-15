from pydantic import ValidationError
from typing import Union
from datetime import datetime, timezone
from unic.utils import time_helpers
from unic.time_unit.validators.models import UnixtimeModelValidator
from unic.time_unit.exceptions.exceptions import UnixtimeValidationError
from unic.core.base_model import BaseModel


class UnixtimeModel(BaseModel):
    def __init__(self):
        super().__init__("timezone")

    def _convert_unixtime(
        self, target_data: str, target_timezone: timezone, unit: str
    ) -> int:
        date_str = target_data[:19]
        millisecond_str = target_data[20:23] if len(target_data) > 19 else "000"

        dt_with_timezone = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=target_timezone
        )

        dt_timestamp = int(dt_with_timezone.timestamp())
        dt_unixtime = (
            f"{dt_timestamp}{millisecond_str}" if unit == "msec" else f"{dt_timestamp}"
        )

        return int(dt_unixtime)

    def convert(self, data: str, tz: Union[str, None] = None, unit: str = "sec") -> int:
        try:
            input_data = UnixtimeModelValidator(data=data, tz=tz, unit=unit)

            target_timezone = time_helpers.get_timezone(
                model_config=self.model_config, tz=tz
            )

            return self._convert_unixtime(
                target_data=input_data.data,
                target_timezone=target_timezone,
                unit=unit,
            )

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise UnixtimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[str], tz: Union[str, None] = None, unit: str = "sec"
    ) -> list[int]:
        if not isinstance(data, list):
            raise TypeError("data must be a list of str")

        try:
            input_data = UnixtimeModelValidator(data=data, tz=tz, unit=unit)

            target_timezone = time_helpers.get_timezone(
                model_config=self.model_config, tz=tz
            )

            return [
                self._convert_unixtime(
                    target_data=data,
                    target_timezone=target_timezone,
                    unit=unit,
                )
                for data in input_data.data
            ]

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise UnixtimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
