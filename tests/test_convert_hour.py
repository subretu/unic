import pytest
from unicorn.unit import timeunit
import importlib


class TestConverterHour:
    def test_convert_hour_msec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(6, from_unit="hour", to_unit="msec")

        assert result == 21600000

    def test_convert_hour_sec(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(4, from_unit="hour", to_unit="sec")

        assert result == 14400

    def test_convert_hour_min(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(7, from_unit="hour", to_unit="min")

        assert result == 420

    def test_convert_hour_min_float(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(7.5, from_unit="hour", to_unit="min")

        assert result == 450

    def test_convert_hour_hour(self):
        test_timeunit = timeunit.TimeUnit()
        result = test_timeunit.convert(24, from_unit="hour", to_unit="hour")

        assert result == 24

    def test_convert_hour_fail(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, from_unit="hour", to_unit="hr")

        # パッケージ名
        package_name = "pydantic_core"
        # パッケージをインポート
        package = importlib.import_module(package_name)
        # パッケージのバージョンを取得
        version = package.__version__

        error_msg = f"""1 validation error for TimeUnitModel
to_unit
  Value error, Invalid to_unit name: hr. Allowed values are ['msec', 'sec', 'min', 'hour']. [type=value_error, input_value='hr', input_type=str]
    For further information visit https://errors.pydantic.dev/{version}/v/value_error"""
        assert str(e.value) == error_msg

    def test_convert_hour_fail_parameter_count_shortage_from_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, to_unit="min")

        error_msg = "The 'from_unit' argument is required."

        assert str(e.value) == error_msg

    def test_convert_hour_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_timeunit = timeunit.TimeUnit()
            _ = test_timeunit.convert(24, from_unit="hour")

        error_msg = "The 'to_unit' argument is required."

        assert str(e.value) == error_msg
