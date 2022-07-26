![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

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
    - string(yyyy-mm-dd hh:mm:ss) / string(yyyy-mm-dd hh:mm:ss)+timezone → unixtime

## Installing
----------

- Local install using pip.

```
git clone https://github.com/subretu/unicorn.git
pip install ./unicorn/
```



## Example
----------------
```python
import unicorn


converter = unicorn.ConvertTimeObject()
dt_timestamp = converter.convert_timestamp(1577841753)
```
