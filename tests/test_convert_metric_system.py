import pytest
import unic


class TestConverterMetricSystem:
    @pytest.mark.parametrize(
        "data, from_unit, to_unit,  expect",
        [
            (1, "nm", "mm", 0.000001),
            (3, "um", "cm", 0.00030000000000000003),
            (5, "mm", "cm", 0.5),
            (15, "mm", "m", 0.015),
            (10, "cm", "mm", 100),
            (20, "cm", "m", 0.2),
            (25, "m", "mm", 25000),
            (50, "m", "cm", 5000),
        ],
    )
    def test_convert_metric_system(self, data, from_unit, to_unit, expect):
        test_metric_system_unit = unic.load_model("metric_system")
        result = test_metric_system_unit.convert(
            data, from_unit=from_unit, to_unit=to_unit
        )

        assert result == expect

    def test_convert_metric_system_fail(self):
        with pytest.raises(Exception) as e:
            test_metric_system_unit = unic.load_model("metric_system")
            _ = test_metric_system_unit.convert(35, from_unit="mm", to_unit="MM")

        error_msg = "Value error, MM is invalid value for parameter: to_unit. Allowed values are ['nm', 'um', 'mm', 'cm', 'm', 'km', 'Mm', 'Gm', 'Tm']."

        assert str(e.value) == error_msg

    def test_convert_metric_system_faill_parameter_count_shortage_from_unit(self):
        with pytest.raises(Exception) as e:
            test_metric_system_unit = unic.load_model("metric_system")
            _ = test_metric_system_unit.convert(10, to_unit="cm")

        assert str(e.value) in [
            "MetricSystemModel.convert() missing 1 required keyword-only argument: 'from_unit'",
            "convert() missing 1 required keyword-only argument: 'from_unit'",
        ]

    def test_convert_metric_system_fail_parameter_count_shortage_to_unit(self):
        with pytest.raises(Exception) as e:
            test_metric_system_unit = unic.load_model("metric_system")
            _ = test_metric_system_unit.convert(100, from_unit="m")

        assert str(e.value) in [
            "MetricSystemModel.convert() missing 1 required keyword-only argument: 'to_unit'",
            "convert() missing 1 required keyword-only argument: 'to_unit'",
        ]
