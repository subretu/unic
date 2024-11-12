class DatetimeValidationError(Exception):
    """Custom exception: DatetimeModel validation error"""

    def __init__(self, message: str):
        super().__init__(message)


class UnixtimeValidationError(Exception):
    """Custom exception: UnixtimeModel validation error"""

    def __init__(self, message: str):
        super().__init__(message)


class TimeValidationError(Exception):
    """Custom exception: TimeModel validation error"""

    def __init__(self, message: str):
        super().__init__(message)
