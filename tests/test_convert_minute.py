import pytest
import unic


class TestConverterMinute:
    def test_convert_minute_msec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(60, from_unit="min", to_unit="msec")

        assert result == 3600000

    def test_convert_minute_sec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(568, from_unit="min", to_unit="sec")

        assert result == 34080

    def test_convert_minute_sec_float(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(120.5, from_unit="min", to_unit="sec")

        assert result == 7230

    def test_convert_minute_min(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(60, from_unit="min", to_unit="min")

        assert result == 60

    def test_convert_minute_hour(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(120, from_unit="min", to_unit="hour")

        assert result == 2

    def test_convert_batch_minute_sec(self):
        test_timeobject = unic.load_model("time")
        result = test_timeobject.convert_batch(
            [568, 120], from_unit="min", to_unit="sec"
        )

        assert result == [34080, 7200]

    def test_convert_minute_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(60, from_unit="min", to_unit="minute")

        error_msg = "Value error, minute is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."

        assert str(e.value) == error_msg

    def test_convert_minute_fail_parameter_count_shortage(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, to_unit="sec")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'from_unit'",
            "convert() missing 1 required keyword-only argument: 'from_unit'",
        ]

    def test_convert_minute_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="minute")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'to_unit'",
            "convert() missing 1 required keyword-only argument: 'to_unit'",
        ]

    def test_convert_minute_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="minute", to_unit="hr")

        error_msg = "Value error, minute is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour'].; Value error, hr is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg

    def test_convert_batch_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("time")
            _ = test_timeobject.convert_batch(
                [568, 120], from_unit="minute", to_unit="hour"
            )

        error_msg = "Value error, minute is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg
