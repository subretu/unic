from ..utils import config_parser


def check_number(parameter: dict) -> None:
    if len(parameter) <= 1:
        pass
    else:
        raise Exception(
            "Too many parameter.If specify parameters to the function,the number should be one."
        )


def check_name(parameter_name: dict) -> None:
    if "tz" in parameter_name:
        pass
    else:
        raise Exception("Invalid parameter name.")


def check_value(parameter_value: str) -> None:
    parameter = config_parser.parse_toml("./unicorn/configs/timezone.toml")
    if parameter_value in parameter.keys():
        pass
    else:
        raise Exception("Invalid parameter value.")
