import pytest
from unicorn.unit import timeunit


class TestConverterHour:
    def test_convert_hour_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(6000, "hour", "msec")

        assert result == 0.0016666666666666666

    def test_convert_hour_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(4800, "hour", "sec")

        assert result == 1.3333333333333333

    def test_convert_hour_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(720, "hour", "min")

        assert result == 12

    def test_convert_hour_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(24, "hour", "hour")

        assert result == 24

    def test_convert_hour_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, "hour", "hr")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Undefined unit. (type=value_error)"""
        assert str(e.value) == error_msg
