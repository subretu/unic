from ..config import settings


def check_number(parameter: dict) -> None:
    if len(parameter) <= 1:
        pass
    else:
        raise Exception("Too many parameter.")


def check_name(parameter_name: dict) -> None:
    if (len(parameter_name) == 0) or ("tz" in parameter_name):
        pass
    else:
        raise Exception("Invalid parameter name.")


def check_value(parameter_value: str) -> None:
    if parameter_value in settings.TIMEZONE:
        pass
    else:
        raise Exception("Invalid parameter value.")
