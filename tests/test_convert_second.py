import pytest
import unic


class TestConverterSecond:
    @pytest.mark.parametrize(
        "msec, from_unit, to_unit,  expect",
        [
            (8, "sec", "msec", 8000),
            (9, "sec", "msec", 9000),
            (150, "sec", "msec", 150000),
        ],
    )
    def test_convert_second_msec(self, msec, from_unit, to_unit, expect):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(msec, from_unit=from_unit, to_unit=to_unit)

        assert result == expect

    def test_convert_second_sec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(200, from_unit="sec", to_unit="sec")

        assert result == 200

    def test_convert_second_min(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(180, from_unit="sec", to_unit="min")

        assert result == 3

    def test_convert_second_min_float(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(180.6, from_unit="sec", to_unit="min")

        assert result == 3.01

    def test_convert_second_hour(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(7200, from_unit="sec", to_unit="hour")

        assert result == 2

    def test_convert_batch_second_hour(self):
        test_timeobject = unic.load_model("time")
        result = test_timeobject.convert_batch(
            [3600, 54000], from_unit="sec", to_unit="hour"
        )

        assert result == [1, 15]

    def test_convert_second_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(35, from_unit="sec", to_unit="second")

        error_msg = "Value error, second is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."

        assert str(e.value) == error_msg

    def test_convert_second_fail_parameter_count_shortage(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, to_unit="hour")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'from_unit'",
            "convert() missing 1 required keyword-only argument: 'from_unit'",
        ]

    def test_convert_second_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="second")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'to_unit'",
            "convert() missing 1 required keyword-only argument: 'to_unit'",
        ]

    def test_convert_second_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="second", to_unit="minute")

        error_msg = "Value error, second is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour'].; Value error, minute is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg

    def test_convert_batch_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("time")
            _ = test_timeobject.convert_batch(
                [3600, 54000], from_unit="second", to_unit="min"
            )

        error_msg = "Value error, second is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg
