


# User Guide

This guide provides a concise overview of how to use the `unic` package.

---

## Installation

```bash
pip install unic
```

---

## Time Unit Conversion

The current available conversion targets are as follows.

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

### TimeModel

```python
import unic
convert_model = unic.load_model("time")  # Load TimeModel

# Examples of TimeModel Conversion:

# Single value conversion
convert_model.convert(2, from_unit="hour", to_unit="min")    # 2 hours → minutes
convert_model.convert(2, from_unit="min",  to_unit="sec")    # 2 minutes → seconds
convert_model.convert(2, from_unit="sec",  to_unit="msec")   # 2 seconds → milliseconds
convert_model.convert(2, from_unit="msec", to_unit="hour")   # 2 milliseconds → hours

# List conversion
convert_model.convert([2, 4, 6], from_unit="hour", to_unit="min")
convert_model.convert([2, 4, 6], from_unit="min",  to_unit="sec")
convert_model.convert([2, 4, 6], from_unit="sec",  to_unit="msec")
convert_model.convert([2, 4, 6], from_unit="msec", to_unit="hour")

# Deprecated: convert_batch
convert_model.convert_batch([2,4,6], from_unit="hour", to_unit="min")  # -- deprecated
```

---

### DatetimeModel

```python
import unic
convert_model = unic.load_model("datetime")  # Load DatetimeModel

# Examples of DatetimeModel Conversion:

# Single value conversion
convert_model.convert(1577841753, format="datetime")
convert_model.convert(1577841753, format="datetime", tz="Asia/Tokyo")
convert_model.convert(1577841753, format="date")
convert_model.convert(1577841753, format="date", tz="Asia/Tokyo")

# List conversion
convert_model.convert([1577841753, 1577941753], format="datetime")
convert_model.convert([1577841753, 1577941753], format="datetime", tz="Asia/Tokyo")
convert_model.convert([1577841753, 1577941753], format="date")
convert_model.convert([1577841753, 1577941753], format="date", tz="Asia/Tokyo")

# Deprecated: convert_batch
convert_model.convert_batch([1577841753,1577941753], format="datetime")  # -- deprecated
```

---

### UnixtimeModel

```python
import unic
convert_model = unic.load_model("unixtime")  # Load UnixtimeModel

# Examples of UnixtimeModel Conversion:

# Single value conversion
convert_model.convert("2023-05-12 10:15:20")
convert_model.convert("2023-05-12 10:15:20", unit="sec")
convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")

# List conversion
convert_model.convert(["2023-05-12 10:15:20", "2023-05-13 10:15:20"], tz="Asia/Tokyo")
convert_model.convert(["2023-05-12 10:15:20", "2023-05-13 10:15:20.123"], unit="msec")

# Deprecated: convert_batch
convert_model.convert_batch(["2023-05-12 10:15:20","2023-05-13 10:15:20"], tz="Asia/Tokyo")  # -- deprecated
```

---

## Length Unit Conversion

The current available conversion targets are as follows.

  - MetricSystemModel
    -  Target Metric System Units

       ```
       nm, um, mm, cm, m, km, Mm, Gm, Tm
       ```
       ※ um : represents ㎛.
     -  The target metric system units are can be converted to each other.

### MetricSystemModel

```python
import unic
convert_model = unic.load_model("metric_system")  # Load MetricSystemModel

# Examples of MetricSystemModel Conversion:

# Single value conversion
convert_model.convert(20, from_unit="nm", to_unit="um")
convert_model.convert(20, from_unit="nm", to_unit="mm")
convert_model.convert(20, from_unit="nm", to_unit="cm")
convert_model.convert(20, from_unit="nm", to_unit="m")
convert_model.convert(20, from_unit="nm", to_unit="Mm")
convert_model.convert(20, from_unit="nm", to_unit="Gm")
convert_model.convert(20, from_unit="nm", to_unit="Tm")

# List conversion
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="um")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="mm")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="cm")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="m")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="Mm")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="Gm")
convert_model.convert([20, 50, 100, 200], from_unit="nm", to_unit="Tm")

# Deprecated: convert_batch
convert_model.convert_batch([20,50,100,200], from_unit="nm", to_unit="um")  # -- deprecated
```
