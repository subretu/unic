class ConvertTime:
    def __init__(self):
        pass

    def convert_millisecond(self, data, time_unit):
        try:
            if time_unit == "h":
                return (data / 1000) / 3600
            elif time_unit == "m":
                return (data / 1000) / 60
            elif time_unit == "s":
                return data / 1000
            elif time_unit == "ms":
                return data
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise
