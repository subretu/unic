import pytest
from unicorn.unit import timeunit


class TestConverterSecond:
    def test_convert_second_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(8, from_unit="sec", to_unit="msec")

        assert result == 8000

    @pytest.mark.parametrize(
        "msec, from_unit, to_unit,  expect",
        [
            (8, "sec", "msec", 8000),
            (9, "sec", "msec", 9000),
            (150, "sec", "msec", 150000),
        ],
    )
    def test_convert_second_msec2(self, msec, from_unit, to_unit, expect):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(msec, from_unit=from_unit, to_unit=to_unit)

        assert result == expect

    def test_convert_second_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(200, from_unit="sec", to_unit="sec")

        assert result == 200

    def test_convert_second_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(180, from_unit="sec", to_unit="min")

        assert result == 3

    def test_convert_second_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(7200, from_unit="sec", to_unit="hour")

        assert result == 2

    def test_convert_second_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(35, from_unit="sec", to_unit="second")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Invalid to_unit name: second. Allowed values are ['msec', 'sec', 'min', 'hour']. (type=value_error)"""
        assert str(e.value) == error_msg
