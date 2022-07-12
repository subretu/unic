import pytest
from unicorn.timeunit import convert_timeunit


class TestConverterMillisecond:
    def test_convert_millisecond_msec(self):
        aaa = convert_timeunit.ConvertTimeUnit()
        result_data = aaa.convert_millisecond(6, "msec")

        assert result_data == 6

    def test_convert_millisecond_sec(self):
        aaa = convert_timeunit.ConvertTimeUnit()
        result_data = aaa.convert_millisecond(10, "sec")

        assert result_data == 10000

    def test_convert_millisecond_min(self):
        aaa = convert_timeunit.ConvertTimeUnit()
        result_data = aaa.convert_millisecond(50, "min")

        assert result_data == 3000000

    def test_convert_millisecond_hour(self):
        aaa = convert_timeunit.ConvertTimeUnit()
        result_data = aaa.convert_millisecond(24, "hr")

        assert result_data == 86400000
