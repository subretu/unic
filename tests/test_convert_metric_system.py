import pytest
import unic


class TestConverterMetricSystem:
    @pytest.mark.parametrize(
        "data, from_unit, to_unit,  expect",
        [
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
