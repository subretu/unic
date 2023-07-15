import pytest
from unicorn.unit import timeunit
import importlib


class TestConverterMinute:
    def test_convert_minute_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, from_unit="min", to_unit="msec")

        assert result == 3600000

    def test_convert_minute_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(568, from_unit="min", to_unit="sec")

        assert result == 34080

    def test_convert_minute_sec_float(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(120.5, from_unit="min", to_unit="sec")

        assert result == 7230

    def test_convert_minute_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(60, from_unit="min", to_unit="min")

        assert result == 60

    def test_convert_minute_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(120, from_unit="min", to_unit="hour")

        assert result == 2

    def test_convert_minute_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(60, from_unit="min", to_unit="minute")

        # パッケージ名
        package_name = "pydantic_core"
        # パッケージをインポート
        package = importlib.import_module(package_name)
        # パッケージのバージョンを取得
        version = package.__version__

        error_msg = f"""1 validation error for TimeUnitModel
to_unit
  Value error, Invalid to_unit name: minute. Allowed values are ['msec', 'sec', 'min', 'hour']. [type=value_error, input_value='minute', input_type=str]
    For further information visit https://errors.pydantic.dev/{version}/v/value_error"""
        assert str(e.value) == error_msg

    def test_convert_minute_fail_parameter_count_shortage(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, to_unit="sec")

        error_msg = "The 'from_unit' argument is required."

        assert str(e.value) == error_msg

    def test_convert_minute_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, from_unit="minute")

        error_msg = "The 'to_unit' argument is required."

        assert str(e.value) == error_msg
