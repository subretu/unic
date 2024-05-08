import pytest
import unic


class TestConvertUnixtime:
    def test_convert_unixtime_utc(self):
        test_unixtime = unic.load_model("unixtime")
        result = test_unixtime.convert("2022-07-18 13:49:00")

        assert result == 1658152140

    def test_convert_unixtime_except_milisecond_utc(self):
        test_unixtime = unic.load_model("unixtime")
        result = test_unixtime.convert("2022-07-18 13:49:00.123")

        assert result == 1658152140123

    def test_convert_unixtime_jst(self):
        test_unixtime = unic.load_model("unixtime")
        result = test_unixtime.convert("2022-07-18 13:49:00", tz="Asia/Tokyo")

        assert result == 1658184540

    def test_convert_unixtime_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_unixtime = unic.load_model("unixtime")
            _ = test_unixtime.convert(
                "2022-07-18 13:49:00", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) in [
            "UnixtimeModel.convert() got an unexpected keyword argument 'hoge'",
            "convert() got an unexpected keyword argument 'hoge'",
        ]

    def test_convert_unixtime_parameter_error(self):
        with pytest.raises(Exception) as e:
            test_unixtime = unic.load_model("unixtime")
            _ = test_unixtime.convert("2022/07/18 13:49:00", tz="Asia/Tokyo")

        error_msg = "Value error, '2022/07/18 13:49:00' is invalid date format. Allowed formats are ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f']."
        print(e.value)
        assert str(e.value) == error_msg
