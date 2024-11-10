import pytest
from datetime import datetime, timezone, timedelta
import unic


class TestConvertDatetime:
    def test_convert_datetime_utc_10digits(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494, format="datetime")

        assert result == datetime(2022, 7, 16, 15, 31, 34, tzinfo=timezone.utc)

    def test_convert_datetime_utc_13digits(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494123, format="datetime")

        assert result == datetime(2022, 7, 16, 15, 31, 34, 123000, tzinfo=timezone.utc)

    def test_convert_batch_datetime_utc(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert_batch(
            [1657985494, 1657985494123], format="datetime"
        )

        assert result == [
            datetime(2022, 7, 16, 15, 31, 34, tzinfo=timezone.utc),
            datetime(2022, 7, 16, 15, 31, 34, 123000, tzinfo=timezone.utc),
        ]

    def test_convert_datetime_jst(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494, format="datetime", tz="Asia/Tokyo")

        assert result == datetime(
            2022, 7, 17, 00, 31, 34, tzinfo=timezone(timedelta(seconds=32400))
        )

    def test_convert_datetime_parameter_name_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657985494, format="datetime", timezone="Asia/Tokyo"
            )

        assert str(e.value) in [
            "DatetimeModel.convert() got an unexpected keyword argument 'timezone'",
            "convert() got an unexpected keyword argument 'timezone'",
        ]

    def test_convert_datetime_parameter_value_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494, format="datetime", tz="Asia/Osaka")

        assert (
            str(e.value)
            == "Value error, Asia/Osaka is invalid value for parameter: tz."
        )

    def test_convert_datetime_parameter_value_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494129, format="datatime")

        error_msg = "Value error, datatime is invalid value for parameter: format. Allowed values are ['datetime', 'date']."

        assert str(e.value) == error_msg

    def test_convert_datetime_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657985494, format="datetime", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) in [
            "DatetimeModel.convert() got an unexpected keyword argument 'hoge'",
            "convert() got an unexpected keyword argument 'hoge'",
        ]

    def test_convert_datetime_required_parameter_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494, tz="Asia/Tokyo")

        assert str(e.value) in [
            "DatetimeModel.convert() missing 1 required positional argument: 'format'",
            "convert() missing 1 required positional argument: 'format'",
        ]

    def test_convert_datetime_digits_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(16579854949, format="datetime")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_datetime_digits_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(165798549412, format="datetime")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_datetime_digits_error_patarn3(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(165798549, format="datetime", tz="Asia/Tokyo")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_datetime_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657111198549444, format="datatime", tz="Asia/Tokyo"
            )

        assert (
            str(e.value)
            == "Value error, Unixtime digits is 10 or 13.; Value error, datatime is invalid value for parameter: format. Allowed values are ['datetime', 'date']."
        )

    def test_convert_batch_datetime_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert_batch(
                [1657985494, 1657985494123], format="datatime"
            )

        assert (
            str(e.value)
            == "Value error, datatime is invalid value for parameter: format. Allowed values are ['datetime', 'date']."
        )
