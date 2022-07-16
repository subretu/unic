import pytest
from datetime import datetime, timezone, timedelta
from unicorn.timeobject import timeobject


class TestConvertTimestamp:
    def test_convert_timestamp_utc(self):
        test_timeobject = timeobject.TimeObject()
        result = test_timeobject.convert_timestamp(1657985494)

        assert result == datetime(2022, 7, 16, 15, 31, 34, tzinfo=timezone.utc)

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
