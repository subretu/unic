from unic.utils import config_parser


def check_parameter_count(parameter: dict) -> None:
    if len(parameter) <= 1:
        return
    else:
        raise ValueError(
            "Too many parameter.If specify parameters to the function,the number should be one."
        )


def check_parameter_value(parameter_value: str) -> None:
    parameter = config_parser.parse_toml("timezone")
    if parameter_value in parameter.keys():
        return
    else:
        raise ValueError("Invalid parameter value.")
