import pytest
from unicorn.unit import timeunit


class TestConverterSecond:
    def test_convert_second_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_second(8, "msec")

        assert result == 0.008

    def test_convert_second_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_second(200, "sec")

        assert result == 200

    def test_convert_second_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_second(19, "min")

        assert result == 1140

    def test_convert_second_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_second(4, "hour")

        assert result == 14400

    def test_convert_second_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert_second(35, "second")

        assert str(e.value) == "Undefined unit time."
