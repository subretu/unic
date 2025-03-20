from pydantic import ValidationError
from unic.utils import config_parser
from unic.length_unit.validators.models import MetricSystemModelValidator
from fractions import Fraction
from unic.length_unit.exceptions.exceptions import MetricSystemValidationError


class MetricSystemModel:
    def __init__(self):
        self.metric_system_parameter = config_parser.parse_toml("metirc_system")

    def _convert_metric_system(
        self, target_data: int, target_metric_system_conversion_parameter: str
    ) -> float:
        return float(target_data * Fraction(target_metric_system_conversion_parameter))

    def convert(self, data: int, *, from_unit: str, to_unit: str) -> int:
        try:
            input_data = MetricSystemModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )

            target_metric_system_conversion_parameter = (
                self.metric_system_parameter.get(from_unit, {}).get(to_unit, None)
            )

            return self._convert_metric_system(
                target_data=input_data.data,
                target_metric_system_conversion_parameter=target_metric_system_conversion_parameter,
            )

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)

    def convert_batch(
        self, data: list[str], *, from_unit: str, to_unit: str
    ) -> list[int]:
        if not isinstance(data, list):
            raise TypeError("data must be a list of str")

        try:
            input_data = MetricSystemModelValidator(
                data=data,
                from_unit=from_unit,
                to_unit=to_unit,
            )

            target_metric_system_conversion_parameter = (
                self.metric_system_parameter.get(from_unit, {}).get(to_unit, None)
            )

            return [
                self._convert_metric_system(
                    target_data=data,
                    target_metric_system_conversion_parameter=target_metric_system_conversion_parameter,
                )
                for data in input_data.data
            ]

        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise MetricSystemValidationError(error_messages)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            raise ValueError(error_message)
