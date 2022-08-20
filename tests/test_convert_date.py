import pytest
from datetime import date
from unicorn.timeobject import timeobject


class TestConvertDate:
    def test_convert_date_utc_10digits(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_date(1657985494)

        assert result == date(2022, 7, 16)

    def test_convert_date_utc_13digits(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_date(1657985494123)

        assert result == date(2022, 7, 16)

    def test_convert_date_jst(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_date(1657985494, tz="Asia/Tokyo")

        assert result == date(2022, 7, 17)

    def test_convert_date_parameter_name_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(1657985494, timezone="Asia/Tokyo")

        assert str(e.value) == "Invalid parameter name."

    def test_convert_datetime_parameter_value_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(1657985494, tz="Asia/Osaka")

        assert str(e.value) == "Invalid parameter value."

    def test_convert_date_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(1657985494, tz="Asia/Tokyo", hoge=123456)

        assert str(e.value) == "Too many parameter."

    def test_convert_date_digits_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(16579854949)

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_date_digits_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(165798549412)

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_date_digits_error_patarn3(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_date(165798549, tz="Asia/Tokyo")

        assert str(e.value) == "Unixtime digits is 10 or 13."
