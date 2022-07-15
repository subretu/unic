class TimeUnit:
    def convert_millisecond(self, data, unit):
        try:
            if unit == "msec":
                return data
            elif unit == "sec":
                return data * 1000
            elif unit == "min":
                return data * 60 * 1000
            elif unit == "hr":
                return data * 3600 * 1000
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_second(self, data, unit):
        try:
            if unit == "msec":
                return data / 1000
            elif unit == "sec":
                return data
            elif unit == "min":
                return data * 60
            elif unit == "hr":
                return data * 3600
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_minute(self, data, unit):
        try:
            if unit == "msec":
                return (data / 60) / 1000
            elif unit == "sec":
                return data / 60
            elif unit == "min":
                return data
            elif unit == "hr":
                return data * 3600
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise

    def convert_hour(self, data, unit):
        try:
            if unit == "msec":
                return (data / 3600) / 1000
            elif unit == "sec":
                return data / 3600
            elif unit == "min":
                return data / 60
            elif unit == "hr":
                return data
            else:
                raise Exception("Undefined unit time.")
        except Exception:
            raise
