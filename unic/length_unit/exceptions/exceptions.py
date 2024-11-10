class MetricSystemValidationError(Exception):
    """Custom exception: MetricSystemModel validation error"""

    def __init__(self, message: str):
        super().__init__(message)
