import pytest
from datetime import date
import unic


class TestConvertDate:
    def test_convert_date_utc_10digits(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494, format="date")

        assert result == date(2022, 7, 16)

    def test_convert_date_utc_13digits(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494123, format="date")

        assert result == date(2022, 7, 16)

    def test_convert_date_jst(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert(1657985494, format="date", tz="Asia/Tokyo")

        assert result == date(2022, 7, 17)

    def test_convert_batch_date_utc_13digits(self):
        test_timeobject = unic.load_model("datetime")
        result = test_timeobject.convert_batch(
            [1657985494123, 1658071894000], format="date"
        )

        assert result == [date(2022, 7, 16), date(2022, 7, 17)]

    def test_convert_date_parameter_name_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657985494, format="date", timezone="Asia/Tokyo"
            )

        assert str(e.value) in [
            "DatetimeModel.convert() got an unexpected keyword argument 'timezone'",
            "convert() got an unexpected keyword argument 'timezone'",
        ]

    def test_convert_date_parameter_value_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494, format="date", tz="Asia/Osaka")

        assert (
            str(e.value)
            == "Value error, Asia/Osaka is invalid value for parameter: tz."
        )

    def test_convert_date_parameter_value_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494129, format="data")

        error_msg = "Value error, data is invalid value for parameter: format. Allowed values are ['datetime', 'date']."

        assert str(e.value) == error_msg

    def test_convert_date_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657985494, format="date", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) in [
            "DatetimeModel.convert() got an unexpected keyword argument 'hoge'",
            "convert() got an unexpected keyword argument 'hoge'",
        ]

    def test_convert_date_required_parameter_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(1657985494, tz="Asia/Tokyo")

        assert str(e.value) in [
            "DatetimeModel.convert() missing 1 required positional argument: 'format'",
            "convert() missing 1 required positional argument: 'format'",
        ]

    def test_convert_date_digits_error_patarn1(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(16579854949, format="date")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_date_digits_error_patarn2(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(165798549412, format="date")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_date_digits_error_patarn3(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(165798549, format="date", tz="Asia/Tokyo")

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."

    def test_convert_date_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert(
                1657111198549444, format="date", tz="Asia/Osaka"
            )

        assert (
            str(e.value)
            == "Value error, Unixtime digits is 10 or 13.; Value error, Asia/Osaka is invalid value for parameter: tz."
        )

    def test_convert_batch_date_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("datetime")
            _ = test_timeobject.convert_batch(
                [16579854494123, 1658071894000], format="date"
            )

        assert str(e.value) == "Value error, Unixtime digits is 10 or 13."
