class TimeUnit:
    def convert_millisecond(self, data, time_unit):
        try:
            match time_unit:
                case "msec":
                    return data
                case "sec":
                    return data * 1000
                case "min":
                    return data * 60 * 1000
                case "hr":
                    return data * 3600 * 1000
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_second(self, data, time_unit):
        try:
            match time_unit:
                case "msec":
                    return data / 1000
                case "sec":
                    return data
                case "min":
                    return data * 60
                case "hr":
                    return data * 3600
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_minute(self, data, time_unit):
        try:
            match time_unit:
                case "msec":
                    return (data / 60) / 1000
                case "sec":
                    return data / 60
                case "min":
                    return data
                case "hr":
                    return data * 60
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_hour(self, data, time_unit):
        try:
            match time_unit:
                case "msec":
                    return (data / 3600) / 1000
                case "sec":
                    return data / 3600
                case "min":
                    return data / 60
                case "hr":
                    return data
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise
