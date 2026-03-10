![Python minimum version](https://img.shields.io/badge/Python-3.9%2B-brightgreen)
[![Test-pytest](https://github.com/subretu/unic/actions/workflows/pytest.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/pytest.yml)
[![Format-Ruff](https://github.com/subretu/unic/actions/workflows/format_check.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/format_check.yml)
[![Lint-Ruff](https://github.com/subretu/unic/actions/workflows/lint_check.yml/badge.svg)](https://github.com/subretu/unic/actions/workflows/lint_check.yml)

# unic
`unic` is a lightweight Python package for converting:

- time units (`hour`, `min`, `sec`, `msec`)
- Unix timestamps to `datetime` / `date`
- datetime strings to Unix timestamps
- metric length units (`nm` to `Tm`)

It is designed for simple scripting, data processing, analytics, and timestamp handling.

## Installation

```bash
pip install unic
```

## Quick Start

```python
import unic

# Time conversion
time_model = unic.load_model("time")
print(time_model.convert(2, from_unit="hour", to_unit="min"))  # 120

# Unixtime -> datetime
datetime_model = unic.load_model("datetime")
print(datetime_model.convert(1657985494, format="datetime"))

# String datetime -> unixtime
unixtime_model = unic.load_model("unixtime")
print(unixtime_model.convert("2022-07-18 13:49:00", tz="Asia/Tokyo"))

# Metric system conversion
metric_model = unic.load_model("metric_system")
print(metric_model.convert(1200, from_unit="mm", to_unit="m"))  # 1.2
```

## Supported Conversions

### TimeModel
- `hour` / `min` / `sec` / `msec`

### DatetimeModel
- unixtime -> `datetime.datetime`
- unixtime -> `datetime.date`

### UnixtimeModel
- datetime string -> unixtime
- supported formats:
  - `yyyy-mm-dd hh:mm:ss`
  - `yyyy/mm/dd hh:mm:ss`

### MetricSystemModel
- metric length units:
  - `nm`, `um`, `mm`, `cm`, `m`, `km`, `Mm`, `Gm`, `Tm`

## Examples

### Convert a single value
```python
import unic

model = unic.load_model("time")
result = model.convert(7.5, from_unit="hour", to_unit="min")
print(result)  # 450
```

### Convert a list of values
```python
import unic

model = unic.load_model("time")
result = model.convert([2, 4, 6], from_unit="hour", to_unit="min")
print(result)  # [120, 240, 360]
```

### Convert unixtime to datetime
```python
import unic

model = unic.load_model("datetime")
result = model.convert(1657985494, format="datetime", tz="Asia/Tokyo")
print(result)
```

### Convert datetime string to unixtime
```python
import unic

model = unic.load_model("unixtime")
result = model.convert("2022-07-18 13:49:00.123", unit="msec")
print(result)
```

## Notes

- `convert()` supports both single values and lists.
- `convert_batch()` is deprecated. Please use `convert()` with a list instead.
- If `unit` is omitted in `UnixtimeModel`, the default is `sec`.

## Documentation

- See `docs/UserGuide.md`
- Add future pages:
  - `docs/QuickStart.md`
  - `docs/SupportedConversions.md`
  - `docs/FAQ.md`
  - `docs/MigrationGuide.md`

## Why unic?

- Simple API
- Lightweight package
- Supports list conversion
- Supports timezone-aware conversion
- Tested with multiple Python versions

## License

MIT
