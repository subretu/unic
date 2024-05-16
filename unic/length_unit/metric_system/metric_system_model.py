from pydantic import ValidationError
from unic.utils import config_parser
from unic.length_unit.validators import validators
from fractions import Fraction


class MetricSystemModel:
    def convert(self, data: int, *, from_unit: str, to_unit: str) -> int:
        try:
            input_data = validators.MetricSystemModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        parameter = config_parser.parse_toml("metirc_system")
        data = float(input_data.data * Fraction(parameter[from_unit][to_unit]))

        return data
