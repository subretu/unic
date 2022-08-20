import pytest
from unicorn.unixtime import unixtime


class TestConvertUnixtime:
    def test_convert_unixtime_utc(self):
        test_unixtime = unixtime.Unixtime()
        result = test_unixtime.convert_unixtime("2022-07-18 13:49:00")

        assert result == 1658152140

    def test_convert_unixtime_except_milisecond_utc(self):
        test_unixtime = unixtime.Unixtime()
        result = test_unixtime.convert_unixtime("2022-07-18 13:49:00.123")

        assert result == 1658152140123

    def test_convert_unixtime_jst(self):
        test_unixtime = unixtime.Unixtime()
        result = test_unixtime.convert_unixtime("2022-07-18 13:49:00", tz="Asia/Tokyo")

        assert result == 1658184540

    def test_convert_unixtime_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_unixtime = unixtime.Unixtime()
            _ = test_unixtime.convert_unixtime(
                "2022-07-18 13:49:00", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) == "Too many parameter."

    def test_convert_unixtime_parameter_error(self):
        with pytest.raises(Exception) as e:
            test_unixtime = unixtime.Unixtime()
            _ = test_unixtime.convert_unixtime(
                "2022-07-18 13:49:00", timezone="Asia/Tokyo"
            )

        assert str(e.value) == "Invalid parameter name."
