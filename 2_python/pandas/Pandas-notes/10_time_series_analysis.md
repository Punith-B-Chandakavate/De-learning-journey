# 📅 DateTimeIndex and Resampling in Pandas

Pandas provides powerful tools for working with time series data.

Time series operations help analyze data based on dates and time intervals.

---

# 📚 Topics Covered

- 📆 `DateTimeIndex` — Work with time-based data
- 🔄 `resample()` — Change data frequency
- 📈 Time series visualization

---

# 📦 Importing Required Modules

The `pandas` library is used for time series analysis.

The `matplotlib` library is used for plotting charts.

```python
from matplotlib import pyplot as plt
import pandas as pd
import os
```

---

# 📁 Load Dataset

The CSV file is loaded dynamically using the current script directory.

```python
directory = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

file_path = os.path.join(
    directory,
    'datasets',
    'aapl.csv'
)

df = pd.read_csv(
    file_path,
    parse_dates=['Date'],
    index_col='Date'
)

df = df.sort_index()

print(df.head(4))

# Output
#                  Open    High     Low   Close    Volume
# Date
# 2016-07-01      95.49   96.46   95.33   95.89  26026500
# 2016-07-05      95.39   95.40   94.46   94.99  27705200
```

---

# 📆 `DateTimeIndex`

A `DateTimeIndex` allows Pandas to work efficiently with dates and time-based operations.

The `Date` column becomes the DataFrame index.

---

# 🔍 View DateTimeIndex

```python
print(df.index)

# Output
# DatetimeIndex([
#   '2016-07-01',
#   '2016-07-05',
#   '2016-07-06'
# ], dtype='datetime64[ns]', name='Date')
```

---

# 📅 Select Data by Month

You can easily filter data using year and month.

```python
print(df.loc['2017-01'])

# Output
# All records from January 2017
```

---

# 📆 Select Data Between Dates

Date ranges can be selected using slicing.

```python
print(
    df.loc[
        '2017-01-03':'2017-01-05'
    ]
)

# Output
# Records between Jan 3 and Jan 5
```

---

# 🔄 Resampling Time Series Data

The `resample()` method changes the frequency of time series data.

It is commonly used for:

- 📅 Monthly summaries
- 📈 Weekly averages
- 📊 Yearly reports

---

# 📊 Monthly Resampling

The `ME` frequency means Month-End.

The `mean()` method calculates the average closing price for each month.

```python
monthly_df = (
    df.Close
    .resample('ME')
    .mean()
)

print(monthly_df)

# Output
# Date
# 2016-07-31     99.47
# 2016-08-31    107.66
# 2016-09-30    110.85
# 2016-10-31    115.70
```

---

# 📈 Plot Resampled Data

Pandas integrates with Matplotlib for visualization.

```python
df.Close.resample('ME').mean().plot(
    kind='line',
    title='Monthly Resampled DataFrame'
)

plt.show()

# Output
# Line chart of monthly average closing prices
```

---

# 📚 Common Resampling Frequencies

| Frequency | Description |
| --------- | ----------- |
| `'D'`   | Daily       |
| `'W'`   | Weekly      |
| `'ME'`  | Month End   |
| `'MS'`  | Month Start |
| `'Y'`   | Yearly      |
| `'H'`   | Hourly      |

---

# 🎯 Key Points

- 📆 `DateTimeIndex` enables time-based operations
- 🔍 `loc[]` filters data using dates
- 🔄 `resample()` changes data frequency
- 📊 `mean()` calculates average values
- 📈 Resampled data can be visualized easily

---

# ✅ Advantages of Time Series Analysis

- 📅 Easy date-based filtering
- 📊 Better trend analysis
- 📈 Useful for stock and weather data
- ⚡ Efficient time aggregation
- 🚀 Powerful data visualization
- 🔍 Simplifies reporting and forecasting
