# 🧹 Handling Missing Data in Pandas

Missing data is common in real-world datasets.

Pandas provides several methods to detect, fill, remove, and replace missing values efficiently.

---

# 📚 Topics Covered

- 🩹 `fillna()` — Fill missing values
- 🗑 `dropna()` — Remove missing values
- 🔍 `isna()` / `notna()` — Detect missing values
- 📈 `interpolate()` — Fill values using interpolation
- 🔄 `replace()` — Replace specific values

---

# 📦 Importing Required Modules

The `pandas` library is used for data manipulation.

The `os` module helps manage file paths.

```python
import pandas as pd
import os
```

---

# 📁 Load Dataset

The CSV file is loaded dynamically using the current script directory.

```python
directory = os.path.dirname(
    os.path.abspath(__file__)
)

file_path = os.path.join(
    directory,
    'datasets',
    'weather_data_1.csv'
)

df = pd.read_csv(
    file_path,
    parse_dates=['day']
)

df.set_index('day', inplace=True)

print(df.head())

# Output
#             temperature  windspeed      event
# day
# 2017-01-01         32.0        6.0       Rain
# 2017-01-02          NaN        7.0      Sunny
# 2017-01-03         28.0        NaN       Snow
```

---

# 🩹 `fillna()` — Fill Missing Values

The `fillna()` method replaces missing values with specified values.

---

# 🔢 Fill All Missing Values with 0

```python
df = df.fillna(0)

print(df.head())

# Output
# Missing values replaced with 0
```

---

# 🎯 Fill Specific Columns

Different columns can use different replacement values.

```python
df = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'No Event'
})

print(df.head())

# Output
# Missing values replaced column-wise
```

---

# ⏭ Forward Fill — `ffill()`

The `ffill()` method copies the previous valid value forward.

```python
df = df.ffill()

print(df.head())

# Output
# Missing values filled using previous row values
```

---

# ⏮ Backward Fill — `bfill()`

The `bfill()` method fills missing values using the next valid value.

```python
df = df.bfill()

print(df.head())

# Output
# Missing values filled using next row values
```

---

# 🗑 `dropna()` — Remove Missing Values

The `dropna()` method removes rows or columns containing missing values.

---

# ❌ Drop Rows with Any Missing Value

```python
df = df.dropna()

print(df)

# Output
# Rows with missing values removed
```

---

# 🧹 Drop Rows Where All Values Are Missing

```python
df = df.dropna(how='all')

print(df)

# Output
# Fully empty rows removed
```

---

# 📊 Keep Rows with Minimum Non-Missing Values

The `thresh` parameter keeps rows with at least a specified number of valid values.

```python
df = df.dropna(thresh=2)

print(df)

# Output
# Rows with at least 2 non-missing values
```

---

# 🌡 Drop Rows Based on Specific Columns

```python
df = df.dropna(subset=['temperature'])

print(df)

# Output
# Rows with missing temperature removed
```

---

# 🔍 `isna()` — Detect Missing Values

The `isna()` method returns a boolean DataFrame indicating missing values.

```python
missing_mask = df.isna()

print(missing_mask.head())

# Output
# True  -> Missing value
# False -> Valid value
```

---

# ✅ `notna()` — Detect Non-Missing Values

The `notna()` method returns `True` for valid values.

```python
not_missing_mask = df.notna()

print(not_missing_mask.head())

# Output
# True  -> Valid value
# False -> Missing value
```

---

# 📈 `interpolate()` — Fill Missing Values Automatically

Interpolation estimates missing numeric values mathematically.

---

# 📊 Linear Interpolation

```python
df[['temperature', 'windspeed']] = (
    df[['temperature', 'windspeed']]
    .interpolate()
)

print(df)

# Output
# Missing numeric values filled linearly
```

---

# ⏰ Time-Based Interpolation

Time interpolation works using the datetime index.

```python
df[['temperature', 'windspeed']] = (
    df[['temperature', 'windspeed']]
    .interpolate(method='time')
)

print(df)

# Output
# Missing values filled using time intervals
```

---

# 🔄 `replace()` — Replace Specific Values

The `replace()` method changes specified values into new values.

---

# 🚫 Replace Invalid Strings with `pd.NA`

```python
df = df.replace('NaN', pd.NA)

print(df)

# Output
# 'NaN' strings converted to pandas NA
```

---

# 🔢 Replace Numeric Missing Indicators

```python
df = df.replace(-9999, pd.NA)

print(df)

# Output
# -9999 replaced with NA
```

---

# 📋 Replace Multiple Values

```python
df = df.replace(
    [-9999, -8888],
    pd.NA
)

print(df)

# Output
# Multiple invalid values replaced
```

---

# 🎯 Column-Wise Replacement

```python
df = df.replace({
    'temperature': {
        pd.NA: 'Missing'
    },
    'windspeed': {
        pd.NA: 'Missing'
    },
    'event': {
        pd.NA: 'Missing'
    }
})

print(df)

# Output
# Missing values replaced column-wise
```

---

# 🧪 Replace Using NumPy `np.nan`

NumPy's `np.nan` is another standard missing value representation.

```python
import numpy as np

df.replace(-9999, np.nan)

print(df)

# Output
# -9999 replaced with np.nan
```

---

# 🔤 Replace Using Regex

Regex allows replacing text patterns.

---

# ✂ Remove Alphabetic Characters

```python
df = df.replace(
    r'[A-Za-z]+',
    '',
    regex=True
)

print(df)

# Output
# Alphabetic characters removed
```

---

# 🎯 Replace Regex in Specific Columns

```python
df = df.replace({
    'temperature': r'[A-Za-z]+',
    'windspeed': r'[A-Za-z]+',
}, "", regex=True)

print(df)

# Output
# Alphabetic characters removed from selected columns
```

---

# 🏆 Replace Text Labels with Numeric Scores

```python
df = pd.DataFrame({
    "score": [
        "excellent",
        "good",
        "average",
        "poor",
        "excellent"
    ],
    "student": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve"
    ]
})

df = df.replace(
    ["excellent", "good", "average", "poor"],
    [4, 3, 2, 1]
)

print(df)

# Output
#    score  student
# 0      4    Alice
# 1      3      Bob
# 2      2  Charlie
# 3      1    David
# 4      4      Eve
```

---

# 🎯 Key Points

- 🩹 `fillna()` fills missing values
- 🗑 `dropna()` removes missing data
- 🔍 `isna()` detects missing values
- ✅ `notna()` detects valid values
- 📈 `interpolate()` estimates missing numbers
- 🔄 `replace()` changes specific values
- 🔤 Regex enables pattern-based replacements

---

# ✅ Advantages of Handling Missing Data

- 📊 Improves data quality
- 🚀 Better machine learning performance
- 🔍 More accurate analysis
- 🧹 Cleaner datasets
- ⚡ Prevents calculation errors
