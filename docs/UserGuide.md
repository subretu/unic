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

```

### DatetimeModel

```python
import unic

# Load the DatetimeModel from unic
convert_model = unic.load_model("datetime")

# Examples of DateTime Conversion:

# to datetime
convert_datetime = convert_model.convert(1577841753, target="datetime")
# to datetime with timezone
convert_datetime = convert_model.convert(1577841753, target="datetime", tz="Asia/Tokyo")

# to date
convert_date = convert_model.convert(1577841753, target="date")
# to date with timezone
convert_date = convert_model.convert(1577841753, target="date", tz="Asia/Tokyo")

```

### UnixtimeModel

```python
import unic

# Load the UnixtimeModel from unic
convert_model = unic.load_model("unixtime")

# Examples of Unixtime Conversion:

# to unixtime
convert_unixtime = convert_model.convert("2023-05-12 10:15:20")
# to unixtime with timezone
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")

```