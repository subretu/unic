![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![pytest](https://github.com/subretu/unic/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/pytest.yml)
[![black](https://github.com/subretu/unic/actions/workflows/format.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/format.yml)

# unic
  `unic` is a python package that can convert various units.

## Conversion Targets
- The current available conversion targets are as follows.
### Time Unit
  - TimeModel
    - minute / second / milisecond → hour
    - hour / second / milisecond → minute
    - hour / minute / milisecond → second
    - hour / minute / second → milisecond
  - DatetimeModel
    - unixtime / unixtime+timezone → datetime.datetime
    - unixtime / unixtime+timezone → datetime.date
  - UnixtimeModel
    - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime

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
```

#### DatetimeModel

```python
import unic


convert_model = unic.load_model("datetime")
# Convert to datatime
convert_datetime = convert_model.convert(1577841753, target="datetime")
# Convert to date
convert_datetime = convert_model.convert(1577841753, target="date")
```

#### UnixtimeModel

```python
import unic


convert_model = unic.load_model("unixtime")
# Specify time zone
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
```
