import pytest
from unicorn.unit import timeunit


class TestConverterHour:
    def test_convert_hour_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_hour(6000, "msec")

        assert result == 0.0016666666666666668

    def test_convert_hour_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_hour(4800, "sec")

        assert result == 1.3333333333333333

    def test_convert_hour_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_hour(720, "min")

        assert result == 12

    def test_convert_hour_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_hour(24, "hour")

        assert result == 24

    def test_convert_hour_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert_hour(24, "hr")

        error_msg = """1 validation error for TimeUnitrModel
unit
  Undefined unit. (type=value_error)"""
        assert str(e.value) == error_msg
