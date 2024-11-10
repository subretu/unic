import pytest
import unic


class TestConverterMetricSystem:
    @pytest.mark.parametrize(
        "input_data, from_unit, to_unit,  expect",
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
    def test_convert_metric_system_normal(self, input_data, from_unit, to_unit, expect):
        test_metric_system_unit = unic.load_model("metric_system")
        result = test_metric_system_unit.convert(
            input_data, from_unit=from_unit, to_unit=to_unit
        )

        assert result == expect

    @pytest.mark.parametrize(
        "input_data, from_unit, to_unit,  expect",
        [
            ([1, 30, 50], "um", "cm", [0.0001, 0.003, 0.005]),
            ([10, 45, 125], "cm", "mm", [100, 450, 1250]),
            ([20, 68, 216], "um", "cm", [0.002, 0.0068000000000000005, 0.0216]),
        ],
    )
    def test_convert_batch_metric_system_normal(
        self, input_data, from_unit, to_unit, expect
    ):
        test_metric_system_unit = unic.load_model("metric_system")
        result = test_metric_system_unit.convert_batch(
            input_data, from_unit=from_unit, to_unit=to_unit
        )

        assert result == expect

    @pytest.mark.parametrize(
        "input_data, from_unit, to_unit,  error_msg",
        [
            (
                35,
                "mm",
                "MM",
                "Value error, MM is invalid value for parameter: to_unit. Allowed values are ['nm', 'um', 'mm', 'cm', 'm', 'km', 'Mm', 'Gm', 'Tm'].",
            ),
            (
                35,
                "CM",
                "MM",
                "Value error, CM is invalid value for parameter: from_unit. Allowed values are ['nm', 'um', 'mm', 'cm', 'm', 'km', 'Mm', 'Gm', 'Tm'].; Value error, MM is invalid value for parameter: to_unit. Allowed values are ['nm', 'um', 'mm', 'cm', 'm', 'km', 'Mm', 'Gm', 'Tm'].",
            ),
        ],
    )
    def test_convert_unixtime_error_cases(
        self, input_data, from_unit, to_unit, error_msg
    ):
        with pytest.raises(Exception) as e:
            test_metric_system_unit = unic.load_model("metric_system")
            _ = test_metric_system_unit.convert(
                input_data, from_unit=from_unit, to_unit=to_unit
            )

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

    def test_convert_batch_metric_system_error(self):
        with pytest.raises(Exception) as e:
            test_metric_system_unit = unic.load_model("metric_system")
            _ = test_metric_system_unit.convert_batch(
                [1, 30, 50], from_unit="um", to_unit="MM"
            )

        assert (
            str(e.value)
            == "Value error, MM is invalid value for parameter: to_unit. Allowed values are ['nm', 'um', 'mm', 'cm', 'm', 'km', 'Mm', 'Gm', 'Tm']."
        )
