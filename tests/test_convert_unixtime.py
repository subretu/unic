import pytest
import unic


@pytest.fixture
def test_unixtime():
    return unic.load_model("unixtime")


class TestConvertUnixtime:
    @pytest.mark.parametrize(
        "input_time, tz, expected",
        [
            ("2022-07-18 13:49:00", None, 1658152140),
            ("2022-07-18 13:49:00.123", None, 1658152140),
            ("2024-06-20 13:49:00", None, 1718891340),
            ("2024-06-20 13:49:00.123", None, 1718891340),
            ("2022-07-18 13:49:00", "Asia/Tokyo", 1658119740),
        ],
    )
    def test_convert_unixtime_normal(self, test_unixtime, input_time, tz, expected):
        result = test_unixtime.convert(input_time, tz=tz)
        assert result == expected

    @pytest.mark.parametrize(
        "input_time, tz, unit, expected",
        [
            ("2022-07-18 13:49:00", None, "sec", 1658152140),
            ("2022-07-18 13:49:00.123", None, "msec", 1658152140123),
            ("2024-06-20 13:49:00", None, "sec", 1718891340),
            ("2024-06-20 13:49:00.123", None, "sec", 1718891340),
            ("2022-07-18 13:49:00", "Asia/Tokyo", "msec", 1658119740000),
        ],
    )
    def test_convert_unixtime_normal_specify_unit(
        self, test_unixtime, input_time, tz, unit, expected
    ):
        result = test_unixtime.convert(input_time, tz=tz, unit=unit)
        assert result == expected

    @pytest.mark.parametrize(
        "input_time_list, tz, expected",
        [
            (
                ["2022-07-18 13:49:00", "2022-07-18 13:49:00.123"],
                None,
                [1658152140, 1658152140],
            ),
            (
                ["2022-07-18 13:49:00", "2022-07-19 13:49:00"],
                "Asia/Tokyo",
                [1658119740, 1658206140],
            ),
        ],
    )
    def test_convert_batch_unixtime_normal(
        self, test_unixtime, input_time_list, tz, expected
    ):
        result = test_unixtime.convert_batch(input_time_list, tz=tz)
        assert result == expected

    def test_convert_unixtime_parameter_number_error(self):
        with pytest.raises(Exception) as e:
            test_unixtime = unic.load_model("unixtime")
            _ = test_unixtime.convert(
                "2022-07-18 13:49:00", tz="Asia/Tokyo", hoge=123456
            )

        assert str(e.value) in [
            "UnixtimeModel.convert() got an unexpected keyword argument 'hoge'",
            "convert() got an unexpected keyword argument 'hoge'",
        ]

    @pytest.mark.parametrize(
        "input_time, tz, error_msg",
        [
            (
                "22/07/18 13:49:00",
                "Asia/Tokyo",
                (
                    "Value error, '22/07/18 13:49:00' is invalid date format. Allowed formats are "
                    "['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M:%S.%f']."
                ),
            ),
            (
                "22/07/18 13:49:00",
                "Asia/Osaka",
                (
                    "Value error, '22/07/18 13:49:00' is invalid date format. Allowed formats are "
                    "['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M:%S.%f'].; "
                    "Value error, Asia/Osaka is invalid value for parameter: tz."
                ),
            ),
        ],
    )
    def test_convert_unixtime_error_cases(
        self, test_unixtime, input_time, tz, error_msg
    ):
        with pytest.raises(Exception) as e:
            _ = test_unixtime.convert(input_time, tz=tz)
        assert str(e.value) == error_msg

    def test_convert_batch_error(
        self,
        test_unixtime,
    ):
        with pytest.raises(Exception) as e:
            _ = test_unixtime.convert_batch(
                ["22/07/18 13:49:00", "2022-07-18 13:49:00.123"], tz="Asia/Tokyo"
            )

        error_msg = "Value error, '22/07/18 13:49:00' is invalid date format. Allowed formats are ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M:%S.%f']."
        assert str(e.value) == error_msg
