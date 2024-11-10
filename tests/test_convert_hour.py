import pytest
import unic


class TestConverterHour:
    def test_convert_hour_msec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(6, from_unit="hour", to_unit="msec")

        assert result == 21600000

    def test_convert_hour_sec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(4, from_unit="hour", to_unit="sec")

        assert result == 14400

    def test_convert_hour_min(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(7, from_unit="hour", to_unit="min")

        assert result == 420

    def test_convert_hour_min_float(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(7.5, from_unit="hour", to_unit="min")

        assert result == 450

    def test_convert_hour_hour(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(24, from_unit="hour", to_unit="hour")

        assert result == 24

    def test_convert_batch_hour_min(self):
        test_timeobject = unic.load_model("time")
        result = test_timeobject.convert_batch([7, 10], from_unit="hour", to_unit="min")

        assert result == [420, 600]

    def test_convert_hour_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="hour", to_unit="hr")

        error_msg = "Value error, hr is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg

    def test_convert_hour_fail_parameter_count_shortage_from_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, to_unit="min")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'from_unit'",
            "convert() missing 1 required keyword-only argument: 'from_unit'",
        ]

    def test_convert_hour_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="hour")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'to_unit'",
            "convert() missing 1 required keyword-only argument: 'to_unit'",
        ]

    def test_convert_hour_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="hr", to_unit="second")

        error_msg = "Value error, hr is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour'].; Value error, second is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg

    def test_convert_batch_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("time")
            _ = test_timeobject.convert_batch([7, 10], from_unit="hr", to_unit="min")

        error_msg = "Value error, hr is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg
