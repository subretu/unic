<div align="center">
<img src="./images/unicorn.png" width="400">
</div>

# unicorn

- Unicorn is python library for converting various units.
- The current available conversion targets are as follows.
  - Time Unit
    - minute / second / milisecond → hour
    - hour / second / milisecond → minute
    - hour / minute / milisecond → second
    - hour / minutes / second → milisecond
  - TIme Object
    - unixtime / unixtime+timezone → datetime（timestamp format）
    - datetime（timestamp format） / datetime+timezone（timestamp format） → unixtime

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