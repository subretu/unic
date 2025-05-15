from pydantic import ValidationError
from unic.time_unit.validators.models import TimeModelValidator
from fractions import Fraction
from unic.utils import time_helpers
from unic.time_unit.exceptions.exceptions import TimeValidationError
from typing import Union
from unic.core.base_model import BaseModel


class TimeModel(BaseModel):
    def __init__(self):
        super().__init__("timeunit")

    def _convert_time(
        self, target_data: Union[int, float], target_time_conversion_parameter: str
    ) -> float:
        conversion_parameter = (
            float(Fraction(target_time_conversion_parameter))
            if isinstance(target_time_conversion_parameter, str)
            else float(target_time_conversion_parameter)
        )

        return target_data * conversion_parameter

    def convert(self, data: int, *, from_unit: str, to_unit: str) -> float:
        try:
            input_data = TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )

            target_time_conversion_parameter = (
                time_helpers.get_time_unit_conversion_factor(
                    model_config=self.model_config, from_unit=from_unit, to_unit=to_unit
                )
            )

            return self._convert_time(
                target_data=input_data.data,
                target_time_conversion_parameter=target_time_conversion_parameter,
            )

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[Union[int, float]], *, from_unit: str, to_unit: str
    ) -> list[int]:
        if not isinstance(data, list):
            raise TypeError("data must be a list of int or float")

        try:
            input_data = TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )

            target_time_conversion_parameter = (
                time_helpers.get_time_unit_conversion_factor(
                    model_config=self.model_config, from_unit=from_unit, to_unit=to_unit
                )
            )

            return [
                self._convert_time(
                    target_data=data,
                    target_time_conversion_parameter=target_time_conversion_parameter,
                )
                for data in input_data.data
            ]

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise TimeValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
