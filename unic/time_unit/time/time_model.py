from pydantic import ValidationError
from unic.utils import config_parser
from unic.time_unit.validators import validators
from fractions import Fraction
from unic.time_unit.exceptions.exceptions import TimeValidationError
from typing import Union


class TimeModel:
    def __init__(self):
        self.time_unit_parameter = config_parser.parse_toml("timeunit")

    def _convert_time(
        self, target_data: Union[int, float], target_time_conversion_parameter: str
    ) -> int:
        conversion_parameter = (
            float(Fraction(target_time_conversion_parameter))
            if isinstance(target_time_conversion_parameter, str)
            else float(target_time_conversion_parameter)
        )

        return target_data * conversion_parameter

    def convert(self, data: int, *, from_unit: str, to_unit: str) -> float:
        try:
            input_data = validators.TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )

            target_time_conversion_parameter = self.time_unit_parameter.get(
                from_unit, {}
            ).get(to_unit, None)

            converted_data = self._convert_time(
                target_data=input_data.data,
                target_time_conversion_parameter=target_time_conversion_parameter,
            )

            return converted_data

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[int, float], *, from_unit: str, to_unit: str
    ) -> list[int]:
        try:
            input_data = validators.TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )

            target_time_conversion_parameter = self.time_unit_parameter.get(
                from_unit, {}
            ).get(to_unit, None)

            converted_data_list = [
                self._convert_time(
                    target_data=data,
                    target_time_conversion_parameter=target_time_conversion_parameter,
                )
                for data in input_data.data
            ]

            return converted_data_list

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise TimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
