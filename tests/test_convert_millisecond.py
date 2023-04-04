import pytest
from unicorn.unit import timeunit


class TestConverterMillisecond:
    def test_convert_millisecond_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(6, from_unit="msec", to_unit="msec")

        assert result == 6

    def test_convert_millisecond_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(2000, from_unit="msec", to_unit="sec")

        assert result == 2

    def test_convert_millisecond_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(120000, from_unit="msec", to_unit="min")

        assert result == 2

    def test_convert_millisecond_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(43200000, from_unit="msec", to_unit="hour")

        assert result == 12

    def test_convert_millisecond_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(15, from_unit="msec", to_unit="millisec")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Invalid to_unit name: millisec. Allowed values are ['msec', 'sec', 'min', 'hour']. (type=value_error)"""
        assert str(e.value) == error_msg
