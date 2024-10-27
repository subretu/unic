class DatetimeValidationError(Exception):
    """Custom exception: DatetimeModel validation error"""

    def __init__(self, message: str):
        super().__init__(message)
