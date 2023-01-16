import pytest
from unicorn.unit import timeunit
import os


class TestConverterMillisecond:
    def test_convert_millisecond_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_millisecond(6, "msec", "msec")

        assert result == 6

    def test_convert_millisecond_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_millisecond(10, "msec", "sec")

        assert result == 10000

    def test_convert_millisecond_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_millisecond(50, "msec", "min")

        assert result == 3000000

    def test_convert_millisecond_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_millisecond(24, "msec", "hour")

        assert result == 86400000

    def test_convert_millisecond_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert_millisecond(15, "msec", "millisec")

        error_msg = """1 validation error for TimeUnitrModel
unit
  Undefined unit. (type=value_error)"""
        assert str(e.value) == error_msg
