![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![pytest](https://github.com/subretu/unicorn/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unicorn/actions/workflows/pytest.yml)
[![black](https://github.com/subretu/unicorn/actions/workflows/format.yml/badge.svg)](https://github.com/subretu/unicorn/actions/workflows/format.yml)

# unicorn
- Unicorn is various units converting python library.
- The current available conversion targets are as follows.
  - Time Unit
    - minute / second / milisecond → hour
    - hour / second / milisecond → minute
    - hour / minute / milisecond → second
    - hour / minute / second → milisecond
  - TIme Object
    - unixtime / unixtime+timezone → datetime.datetime
    - unixtime / unixtime+timezone → datetime.date
  - Unix Time
    - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime

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
