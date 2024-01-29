from pydantic import ValidationError
from unic.utils import config_parser, validators
from fractions import Fraction


class TimeModel:
    def convert(self, data: int, *, from_unit: str = None, to_unit: str = None) -> int:
        try:
            self.check_parameter_count(from_unit, to_unit)
            input_data = validators.TimeModelValidator(
                data=data, from_unit=from_unit, to_unit=to_unit
            )
        except ValidationError as e:
            raise ValueError(e.errors()[0]["msg"])

        parameter = config_parser.parse_toml("timeunit")
        data = float(input_data.data * Fraction(parameter[from_unit][to_unit]))

        return data

    def check_parameter_count(self, from_unit: str, to_unit: str) -> None:
        if from_unit is None and to_unit is None:
            raise ValueError("Both 'from_unit' and 'to_unit' arguments are required.")
        if from_unit is None or to_unit is None:
            raise ValueError(
                f"The '{'from_unit' if from_unit is None else 'to_unit'}' argument is required."
            )
