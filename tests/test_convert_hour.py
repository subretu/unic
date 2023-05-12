import pytest
from unicorn.unit import timeunit


class TestConverterHour:
    def test_convert_hour_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(6, from_unit="hour", to_unit="msec")

        assert result == 21600000

    def test_convert_hour_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(4, from_unit="hour", to_unit="sec")

        assert result == 14400

    def test_convert_hour_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(7, from_unit="hour", to_unit="min")

        assert result == 420

    def test_convert_hour_min2(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(7.5, from_unit="hour", to_unit="min")

        assert result == 450

    def test_convert_hour_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(24, from_unit="hour", to_unit="hour")

        assert result == 24

    def test_convert_hour_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, from_unit="hour", to_unit="hr")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Invalid to_unit name: hr. Allowed values are ['msec', 'sec', 'min', 'hour']. (type=value_error)"""
        assert str(e.value) == error_msg

    def test_convert_hour_fail_parameter_count_shortage(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, to_unit="hour")

        error_msg = "The 'from_unit' argument is required."

        assert str(e.value) == error_msg
