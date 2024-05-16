from pydantic import ValidationError
from unic.utils import config_parser
from unic.time_unit.validators import validators
from fractions import Fraction


class TimeModel:
    def convert(self, data: int, *, from_unit: str, to_unit: str) -> int:
        try:
            input_data = validators.TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        parameter = config_parser.parse_toml("timeunit")
        data = float(input_data.data * Fraction(parameter[from_unit][to_unit]))

        return data
