![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![pytest](https://github.com/subretu/unicorn/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unicorn/actions/workflows/pytest.yml)
[![black](https://github.com/subretu/unicorn/actions/workflows/format.yml/badge.svg)](https://github.com/subretu/unicorn/actions/workflows/format.yml)

# unicorn
- Unicorn is various units converting python library.
- The current available conversion targets are as follows.
  - Time Unit
    | from | to |
    |--------|------|
    | milisecond | second <br> minute <br> hour |
    | second  | milisecond <br> minute <br> hour  |
    | minute | milisecond <br> second <br> hour  |
    | hour | milisecond <br> second <br> minute  |
  - TIme Object
    | from | to |
    |--------|------|
    | unixtime <br> unixtime+timezone | datetime.datetime |
    | unixtime <br> unixtime+timezone | datetime.date |
  - Unix Time
    | from | to |
    |--------|------|
    | string(yyyy-mm-dd hh:mm:ss) <br> string(yyyy-mm-dd hh:mm:ss)+timezone |  unixtime|

## Installing

- Local install using pip.

```
git clone https://github.com/subretu/unicorn.git
pip install ./unicorn/
```



## Example

```python
import unicorn


converter = unicorn.TimeObject()
dt_timestamp = converter.convert(1577841753, target="datetime")
```
