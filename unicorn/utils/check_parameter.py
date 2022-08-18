from ..config import settings


def check_parameter_value(parameter_value):
    if (parameter_value in settings.TIMEZONE):
        pass
    else:
        raise Exception("Invalid parameter value.")
