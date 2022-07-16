import pytest
from datetime import datetime, timezone, timedelta
from unicorn.timeobject import timeobject


class TestConvertTimestamp:
    def test_convert_timestamp_utc_10digits(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_timestamp(1657985494)

        assert result == datetime(2022, 7, 16, 15, 31, 34, tzinfo=timezone.utc)

    def test_convert_timestamp_utc_13digits(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_timestamp(1657985494123)

        assert result == datetime(2022, 7, 16, 15, 31, 34, 123000, tzinfo=timezone.utc)

    def test_convert_timestamp_jst(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_timestamp(1657985494, tz="Asia/Tokyo")

        assert result == datetime(
            2022, 7, 17, 00, 31, 34, tzinfo=timezone(timedelta(seconds=32400))
        )

    def test_convert_timestamp_parameter_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_timestamp(1657985494, timezone="Asia/Tokyo")

        assert str(e.value) == "Parameter name not defined."

    def test_convert_timestamp_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_timestamp(
                1657985494, tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) == "Too many parameter."

    def test_convert_timestamp_digits_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_timestamp(16579854949)

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_timestamp_digits_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_timestamp(165798549412)

        assert str(e.value) == "Unixtime digits is 10 or 13."

    def test_convert_timestamp_digits_error_patarn3(self):
        with pytest.raises(Exception) as e:
            test_timeobject = timeobject.TimeObject()
            _ = test_timeobject.convert_timestamp(165798549, tz="Asia/Tokyo")

        assert str(e.value) == "Unixtime digits is 10 or 13."
