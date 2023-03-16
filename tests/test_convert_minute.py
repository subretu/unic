import pytest
from unicorn.unit import timeunit


class TestConverterMinute:
    def test_convert_minute_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, from_unit="min", to_unit="msec")

        assert result == 0.001

    def test_convert_minute_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(568, from_unit="min", to_unit="sec")

        assert result == 9.466666666666667

    def test_convert_minute_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, from_unit="min", to_unit="min")

        assert result == 60

    def test_convert_minute_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(17, from_unit="min", to_unit="hour")

        assert result == 1020

    def test_convert_minute_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(60, from_unit="min", to_unit="minute")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Invalid to_unit name: minute. Allowed values are ['msec', 'sec', 'min', 'hour']. (type=value_error)"""
        assert str(e.value) == error_msg
