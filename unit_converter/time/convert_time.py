class ConvertTime:
    def __init__(self):
        pass

    def convert_millisecond(self, data, time_unit):
        try:
            match time_unit:
                case "h":
                    return (data / 1000) / 3600
                case "m":
                    return (data / 1000) / 60
                case "s":
                    return data / 1000
                case "ms":
                    return data
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise
