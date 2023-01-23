import pytest
from unicorn.unit import timeunit


class TestConverterSecond:
    def test_convert_second_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(8, from_unit="sec", to_unit="msec")

        assert result == 0.008

    @pytest.mark.parametrize(
        "msec, from_unit, to_unit,  expect",
        [
            (8, "sec", "msec", 0.008),
            (9, "sec", "msec", 0.009000000000000001),
            (10, "sec", "msec", 0.01),
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
        result = test_timeunit.convert(19, from_unit="sec", to_unit="min")

        assert result == 1140

    def test_convert_second_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(4, from_unit="sec", to_unit="hour")

        assert result == 14400

    def test_convert_second_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(35, from_unit="sec", to_unit="second")

        error_msg = """1 validation error for TimeUnitModel
to_unit
  Undefined unit. (type=value_error)"""
        assert str(e.value) == error_msg
