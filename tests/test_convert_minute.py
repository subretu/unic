import pytest
from unicorn.unit import timeunit


class TestConverterMinute:
    def test_convert_minute_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_minute(60, "msec")

        assert result == 0.001

    def test_convert_minute_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_minute(568, "sec")

        assert result == 9.466666666666667

    def test_convert_minute_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_minute(60, "min")

        assert result == 60

    def test_convert_minute_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert_minute(17, "hr")

        assert result == 1020

    def test_convert_minute_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert_minute(60, "minute")

        assert str(e.value) == "Undefined unit time."
