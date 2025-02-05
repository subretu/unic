![Python minimum version](https://img.shields.io/badge/Python-3.9%2B-brightgreen)
[![Test-pytest](https://github.com/subretu/unic/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/pytest.yml)
[![Format-Ruff](https://github.com/subretu/unic/actions/workflows/format_check.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/format_check.yml)
[![Lint-Ruff](https://github.com/subretu/unic/actions/workflows/lint_check.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/lint_check.yml)

# unic
  `unic` is a python package that can convert various units.

## Conversion Targets
- The current available conversion targets are as follows.

  <details>
  <summary>Time Unit</summary>

    - TimeModel
      - minute / second / milisecond → hour
      - hour / second / milisecond → minute
      - hour / minute / milisecond → second
      - hour / minute / second → milisecond
    - DatetimeModel
      - unixtime / unixtime+timezone → datetime.datetime
      - unixtime / unixtime+timezone → datetime.date
    - UnixtimeModel
      - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime(default is seconds)
      - string(yyyy/mm/dd hh:mm:ss) / string(yyyy/mm/dd hh:mm:ss)+timezone → unixtime(default is seconds)
  </details>

  <details>
  <summary>Length Unit</summary>

    - MetricSystemModel
      -  Target Metric System Units

         ```
         nm, um, mm, cm, m, km, Mm, Gm, Tm
         ```
         ※ um : represents ㎛.
       -  The target metric system units are can be converted to each other.

  </details>

## Installing

  ```
  pip install unic
  ```

## How to
- See the [UserGuide](docs/UserGuide.md).

## Example
### Time Unit
#### TimeModel

```python
import unic


convert_model = unic.load_model("time")
# Convert hour to minute
convert_min = convert_model.convert(2, from_unit="hour", to_unit="min")
# Convert hour to minute (batch processing)
convert_min = convert_model.convert_batch([2,4,6], from_unit="hour", to_unit="min")
```

#### DatetimeModel

```python
import unic


convert_model = unic.load_model("datetime")
# Convert to datatime
convert_datetime = convert_model.convert(1577841753, format="datetime")
# Convert to datatime (batch processing)
convert_datetime = convert_model.convert_batch([1577841753,1577941753], format="datetime")

# Convert to date
convert_datetime = convert_model.convert(1577841753, format="date")
```

#### UnixtimeModel

```python
import unic


convert_model = unic.load_model("unixtime")
# Specify time zone
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
# Specify unit(if not specified, the unit defaults to seconds)
convert_unixtime = convert_model.convert("2023-05-12 10:15:20.123", tz="Asia/Tokyo", unit="msec")
# Specify time zone (batch processing)
convert_unixtime = convert_model.convert_batch(["2023-05-12 10:15:20","2023-05-13 10:15:20","2023-05-14 10:15:20"], tz="Asia/Tokyo")
```

### Length Unit
#### MetricSystemModel

```python
import unic


convert_model = unic.load_model("metric_system")
# Convert cm to m
convert_m = convert_model.convert(20, from_unit="cm", to_unit="m")
# Convert cm to m (batch processing)
convert_m = convert_model.convert_batch([20,50,100,200], from_unit="cm", to_unit="m")
```