class ConvertTime:
    def convert_millisecond(self, msec, time_unit):
        try:
            match time_unit:
                case "h":
                    return (msec / 1000) / 3600
                case "m":
                    return (msec / 1000) / 60
                case "s":
                    return msec / 1000
                case "ms":
                    return msec
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_second(self, sec, time_unit):
        try:
            match time_unit:
                case "h":
                    return sec / 3600
                case "m":
                    return sec / 60
                case "s":
                    return sec
                case "ms":
                    return sec * 1000
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_minutes(self, min, time_unit):
        try:
            match time_unit:
                case "h":
                    return min / 60
                case "m":
                    return min
                case "s":
                    return min * 60
                case "ms":
                    return min * 60 * 1000
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_hour(self, hr, time_unit):
        try:
            match time_unit:
                case "h":
                    return hr
                case "m":
                    return hr * 60
                case "s":
                    return hr * 3600
                case "ms":
                    return hr * 3600 * 1000
                case _:
                    raise Exception("Undefined unit time.")
        except Exception:
            raise
