from pydantic import ValidationError
from unic.utils import config_parser
from unic.length_unit.validators import validators
from fractions import Fraction


class MetricSystemModel:
    def __init__(self):
        self.metric_system_parameter = config_parser.parse_toml("metirc_system")

    def convert(self, data: int, *, from_unit: str, to_unit: str) -> int:
        try:
            input_data = validators.MetricSystemModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        parameter = self.metric_system_parameter.get(from_unit, {}).get(to_unit, None)
        data = float(input_data.data * Fraction(parameter))

        return data
