from pydantic import ValidationError
from unic.utils import config_parser
from unic.time_unit.validators import validators
from fractions import Fraction


class TimeModel:
    def __init__(self):
        self.time_unit_parameter = config_parser.parse_toml("timeunit")

    def convert(self, data: int, *, from_unit: str, to_unit: str) -> float:
        try:
            input_data = validators.TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )
        except ValidationError as e:
            error_messages = "; ".join(err["msg"] for err in e.errors())
            raise ValueError(error_messages)

        parameter = self.time_unit_parameter.get(from_unit, {}).get(to_unit, None)

        conversion_parameter = (
            float(Fraction(parameter))
            if isinstance(parameter, str)
            else float(parameter)
        )

        return input_data.data * conversion_parameter
