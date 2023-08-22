import pytest
from datetime import datetime, timezone, timedelta
from unic.time_unit.datetime import datetime_model


class TestConvertDatetime:
    def test_convert_datetime_utc_10digits(self):
        test_timeobject = datetime_model.DatetimeModel()
        result = test_timeobject.convert(1657985494, target="datetime")

        assert result == datetime(2022, 7, 16, 15, 31, 34, tzinfo=timezone.utc)

    def test_convert_datetime_utc_13digits(self):
        test_timeobject = datetime_model.DatetimeModel()
        result = test_timeobject.convert(1657985494123, target="datetime")

        assert result == datetime(2022, 7, 16, 15, 31, 34, 123000, tzinfo=timezone.utc)

    def test_convert_datetime_jst(self):
        test_timeobject = datetime_model.DatetimeModel()
        result = test_timeobject.convert(1657985494, target="datetime", tz="Asia/Tokyo")

        assert result == datetime(
            2022, 7, 17, 00, 31, 34, tzinfo=timezone(timedelta(seconds=32400))
        )

    def test_convert_datetime_parameter_name_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(
                1657985494, target="datetime", timezone="Asia/Tokyo"
            )

        assert str(e.value) == "Invalid parameter name."

    def test_convert_datetime_parameter_value_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(1657985494, target="datetime", tz="Asia/Osaka")

        assert str(e.value) == "Value error, Asia/Osaka is Invalid value for parameter:tz."

    def test_convert_datetime_parameter_value_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(1657985494129, target="datatime")

        error_msg = "Value error, datatime is Invalid value for parameter:target. Allowed values are ['datetime', 'date']."

        assert str(e.value) == error_msg

    def test_convert_datetime_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(
                1657985494, target="datetime", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) == "Invalid parameter name."

    def test_convert_datetime_digits_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(16579854949, target="datetime")

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_datetime_digits_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(165798549412, target="datetime")

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_datetime_digits_error_patarn3(self):
        with pytest.raises(Exception) as e:
            test_timeobject = datetime_model.DatetimeModel()
            _ = test_timeobject.convert(165798549, target="datetime", tz="Asia/Tokyo")

        assert str(e.value) == "Unixtime digits is 10 or 13."
