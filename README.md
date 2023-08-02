![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![pytest](https://github.com/subretu/unic/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/pytest.yml)
[![black](https://github.com/subretu/unic/actions/workflows/format.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/format.yml)

# unic
- unic is a Python package that can convert various units.
- The current available conversion targets are as follows.
  - Time Unit
    - minute / second / milisecond → hour
    - hour / second / milisecond → minute
    - hour / minute / milisecond → second
    - hour / minute / second → milisecond
  - Time Object
    - unixtime / unixtime+timezone → datetime.datetime
    - unixtime / unixtime+timezone → datetime.date
  - Unix Time
    - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime

## Installing

  - Local install using pip.

  ```
  git clone https://github.com/subretu/unic.git
  pip install ./unic/
  ```



## Example

### Time Unit

```python
import unic


converter = unic.TimeUnit()
# Convert hour to minute
converte_min = converter.convert(2, from_unit="hour", to_unit="min")
```

### Time Object

```python
import unic


converter = unic.TimeObject()
# Convert to datatime
converte_datetime = converter.convert(1577841753, target="datetime")
```

### Unix Time

```python
import unic


converter = unic.Unixtime()
# Specify time zone
converte_unixtime = converter.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
```
