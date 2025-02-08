# User Guide for unic

This guide provides instructions on utilizing the `unic`.

## Installation

`unic` is installed by executing the following command:

```bash
pip install unic
```


## Time Unit Conversion
### TimeModel

```python
import unic

# Load the TimeModel from unic
convert_model = unic.load_model("time")

# Examples of TimeUnit Conversion:

# hour to minute
convert_min = convert_model.convert(2, from_unit="hour", to_unit="min")
# hour to second
convert_sec = convert_model.convert(2, from_unit="hour", to_unit="sec")
# hour to millisecond
convert_msec = convert_model.convert(2, from_unit="hour", to_unit="msec")

# minute to hour
convert_hour = convert_model.convert(2, from_unit="min", to_unit="hour")
# minute to second
convert_sec = convert_model.convert(2, from_unit="min", to_unit="sec")
# minute to millisecond
convert_msec = convert_model.convert(2, from_unit="min", to_unit="msec")

# second to hour
convert_hour = convert_model.convert(2, from_unit="sec", to_unit="hour")
# second to minute
convert_min = convert_model.convert(2, from_unit="sec", to_unit="min")
# second to millisecond
convert_msec = convert_model.convert(2, from_unit="sec", to_unit="msec")

# millisecond to hour
convert_hour = convert_model.convert(2, from_unit="msec", to_unit="hour")
# millisecond to minute
convert_min = convert_model.convert(2, from_unit="msec", to_unit="min")
# millisecond to second
convert_sec = convert_model.convert(2, from_unit="msec", to_unit="sec")

# hour to minute (batch processing)
convert_min = convert_model.convert_batch([2,4,6], from_unit="hour", to_unit="min")
```

### DatetimeModel

```python
import unic

# Load the DatetimeModel from unic
convert_model = unic.load_model("datetime")

# Examples of DateTime Conversion:

# to datetime
convert_datetime = convert_model.convert(1577841753, format="datetime")
# to datetime with timezone
convert_datetime = convert_model.convert(1577841753, format="datetime", tz="Asia/Tokyo")

# to date
convert_date = convert_model.convert(1577841753, format="date")
# to date with timezone
convert_date = convert_model.convert(1577841753, format="date", tz="Asia/Tokyo")

# to datetime (batch processing)
convert_datetime = convert_model.convert_batch([1577841753,1577941753], format="datetime")
```

### UnixtimeModel

```python
import unic

# Load the UnixtimeModel from unic
convert_model = unic.load_model("unixtime")

# Examples of Unixtime Conversion:

# to unixtime
convert_unixtime = convert_model.convert("2023-05-12 10:15:20")
convert_unixtime = convert_model.convert("2023/05/12 10:15:20")
# to unixtime(specify unit, if not specified, the unit defaults to seconds)
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", unit="sec")
convert_unixtime = convert_model.convert("2023/05/12 10:15:20.123", unit="msec")
# to unixtime with timezone
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
convert_unixtime = convert_model.convert("2023/05/12 10:15:20", tz="Asia/Tokyo")
# to unixtime with timezone (batch processing)
convert_unixtime = convert_model.convert_batch(["2023-05-12 10:15:20","2023-05-13 10:15:20"], tz="Asia/Tokyo")
```

## Length Unit Conversion
### MetricSystemModel

```python
import unic

# Load the MetricSystemModel from unic
convert_model = unic.load_model("metric_system")

# Examples of MetricSystem Conversion:

# nm to um
convert_um = convert_model.convert(20, from_unit="nm", to_unit="um")
# nm to mm
convert_mm = convert_model.convert(20, from_unit="nm", to_unit="mm")
# nm to cm
convert_cm = convert_model.convert(20, from_unit="nm", to_unit="cm")
# nm to m
convert_m = convert_model.convert(20, from_unit="nm", to_unit="m")
# nm to Mm
convert_Mm = convert_model.convert(20, from_unit="nm", to_unit="Mm")
# nm to Gm
convert_Gm = convert_model.convert(20, from_unit="nm", to_unit="Gm")
# nm to Tm
convert_Tm = convert_model.convert(20, from_unit="nm", to_unit="Tm")

# nm to um (batch processing)
convert_um = convert_model.convert_batch([20,50,100,200], from_unit="nm", to_unit="um")
```