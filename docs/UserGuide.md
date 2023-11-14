# UserGuide

- The convert procedures using unic are as follows.

## Time Unit
### TimeModel

```python
import unic


convert_model = unic.load_model("time")

# Convert hour to minute
convert_min = convert_model.convert(2, from_unit="hour", to_unit="min")
# Convert hour to second
convert_sec = convert_model.convert(2, from_unit="hour", to_unit="sec")
# Convert hour to milisecond
convert_msec = convert_model.convert(2, from_unit="hour", to_unit="msec")

# Convert minute to hour
convert_hour = convert_model.convert(2, from_unit="min", to_unit="hour")
# Convert minute to second
convert_sec = convert_model.convert(2, from_unit="min", to_unit="sec")
# Convert minute to milisecond
convert_msec = convert_model.convert(2, from_unit="min", to_unit="msec")

# Convert second to hour
convert_hour = convert_model.convert(2, from_unit="sec", to_unit="hour")
# Convert second to minute
convert_min = convert_model.convert(2, from_unit="sec", to_unit="min")
# Convert second to milisecond
convert_msec = convert_model.convert(2, from_unit="sec", to_unit="msec")

# Convert milisecond to hour
convert_hour = convert_model.convert(2, from_unit="msec", to_unit="hour")
# Convert milisecond to minute
convert_min = convert_model.convert(2, from_unit="msec", to_unit="min")
# Convert milisecond to second
convert_sec = convert_model.convert(2, from_unit="msec", to_unit="sec")
```

### DatetimeModel

```python
import unic


convert_model = unic.load_model("datetime")

# Convert to datatime
convert_datetime = convert_model.convert(1577841753, target="datetime")
# Convert to datatime with timezone
convert_datetime = convert_model.convert(1577841753, target="datetime", tz="Asia/Tokyo")

# Convert to date
convert_date = convert_model.convert(1577841753, target="date")
# Convert to date with timezone
convert_date = convert_model.convert(1577841753, target="date", tz="Asia/Tokyo")
```

### UnixtimeModel

```python
import unic


convert_model = unic.load_model("unixtime")

# Convert to unixtime
convert_unixtime = convert_model.convert("2023-05-12 10:15:20")
# Convert to unixtime with timezone
convert_unixtime = convert_model.convert("2023-05-12 10:15:20", tz="Asia/Tokyo")
```