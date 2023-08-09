![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![pytest](https://github.com/subretu/unic/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/pytest.yml)
[![black](https://github.com/subretu/unic/actions/workflows/format.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/format.yml)

# unic
unic is a Python package that can convert various units.

## Conversion Targets
- The current available conversion targets are as follows.
### Time Unit
  - Time
    - minute / second / milisecond → hour
    - hour / second / milisecond → minute
    - hour / minute / milisecond → second
    - hour / minute / second → milisecond
  - Datetime
    - unixtime / unixtime+timezone → datetime.datetime
    - unixtime / unixtime+timezone → datetime.date
  - Unixtime
    - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime

## Installing

  ```
  pip install unic
  ```



## Example
### Time Unit
#### Time

```python
import unic


converter = unic.TimeModel()
# Convert hour to minute
convert_min = converter.convert(2, from_unit="hour", to_unit="min")
```

#### Datetime

```python
import unic


converter = unic.DatetimeModel()
# Convert to datatime
convert_datetime = converter.convert(1577841753, target="datetime")
```

#### Unixtime

```python
import unic


converter = unic.UnixtimeModel()
# Specify time zone
convert_unixtime = converter.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
```
