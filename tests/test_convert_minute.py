import pytest
from unicorn.unit import timeunit


class TestConverterMinute:
    def test_convert_minute_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, "min", "msec")

        assert result == 0.001

    def test_convert_minute_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(568, "min", "sec")

        assert result == 9.466666666666667

    def test_convert_minute_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, "min", "min")

        assert result == 60

    def test_convert_minute_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(17, "min", "hour")

        assert result == 1020

    def test_convert_minute_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(60, "min", "minute")

        error_msg = """1 validation error for TimeUnitrModel
unit
  Undefined unit. (type=value_error)"""
        assert str(e.value) == error_msg
