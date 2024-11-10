import pytest
import unic


class TestConverterMillisecond:
    def test_convert_millisecond_msec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(6, from_unit="msec", to_unit="msec")

        assert result == 6

    def test_convert_millisecond_sec(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(2000, from_unit="msec", to_unit="sec")

        assert result == 2

    def test_convert_millisecond_sec_float(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(1250.6, from_unit="msec", to_unit="sec")

        assert result == 1.2506

    def test_convert_millisecond_min(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(120000, from_unit="msec", to_unit="min")

        assert result == 2

    def test_convert_millisecond_hour(self):
        test_timeunit = unic.load_model("time")
        result = test_timeunit.convert(43200000, from_unit="msec", to_unit="hour")

        assert result == 12

    def test_convert_batch_millisecond_min(self):
        test_timeobject = unic.load_model("time")
        result = test_timeobject.convert_batch(
            [120000, 480000], from_unit="msec", to_unit="min"
        )

        assert result == [2, 8]

    def test_convert_millisecond_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(15, from_unit="msec", to_unit="millisec")

        error_msg = "Value error, millisec is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."

        assert str(e.value) == error_msg

    def test_convert_millisecond_fail_parameter_count_shortage(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, to_unit="min")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'from_unit'",
            "convert() missing 1 required keyword-only argument: 'from_unit'",
        ]

    def test_convert_millisecond_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="msec")

        assert str(e.value) in [
            "TimeModel.convert() missing 1 required keyword-only argument: 'to_unit'",
            "convert() missing 1 required keyword-only argument: 'to_unit'",
        ]

    def test_convert_millisecond_compound_error(self):
        with pytest.raises(Exception) as e:
            test_timeunit = unic.load_model("time")
            _ = test_timeunit.convert(24, from_unit="millisec", to_unit="second")

        error_msg = "Value error, millisec is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour'].; Value error, second is invalid value for parameter: to_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg

    def test_convert_batch_error(self):
        with pytest.raises(Exception) as e:
            test_timeobject = unic.load_model("time")
            _ = test_timeobject.convert_batch(
                [120000, 480000], from_unit="millisec", to_unit="sec"
            )

        error_msg = "Value error, millisec is invalid value for parameter: from_unit. Allowed values are ['msec', 'sec', 'min', 'hour']."
        assert str(e.value) == error_msg
