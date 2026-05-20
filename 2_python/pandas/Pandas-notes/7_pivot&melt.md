# 🔄 Pivoting and Melting DataFrames in Pandas

Pandas provides powerful reshaping functions to transform DataFrames into different formats.

These operations help organize and summarize data efficiently.

---

# 📚 Topics Covered

- 🔄 `pivot()` — Reshape DataFrames
- 📊 `pivot_table()` — Create summary tables
- 🔥 `melt()` — Convert wide data into long format

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
    'pivot_weather_1.csv'
)

df = pd.read_csv(file_path)

print(df)

# Output
#        date      city  temperature  humidity
# 0  5/1/2017  new york           65        56
# 1  5/1/2017    mumbai           75        80
# 2  5/1/2017   beijing           80        26
```

---

# 🔄 Pivoting DataFrames Using `pivot()`

The `pivot()` method reshapes a DataFrame.

It converts unique column values into new columns.

---

# 📊 Basic Pivot Operation

Parameters:

- `index` → Row labels
- `columns` → New column labels
- `values` → Data values

```python
pivot_df = df.pivot(
    index='date',
    columns='city'
)

print(pivot_df)

# Output
#          temperature                 humidity
# city         beijing mumbai new york  beijing mumbai new york
# date
# 5/1/2017          80     75       65       26     80       56
# 5/2/2017          77     78       66       30     83       58
```

---

# 🌡 Pivot Specific Values

The `values` parameter selects specific columns for pivoting.

```python
pivot_df = df.pivot(
    index='date',
    columns='city',
    values='temperature'
)

print(pivot_df)

# Output
# city      beijing  mumbai  new york
# date
# 5/1/2017       80      75        65
# 5/2/2017       77      78        66
# 5/3/2017       79      82        68
```

---

# 📊 Pivot Tables Using `pivot_table()`

The `pivot_table()` method works like `pivot()` but can handle duplicate values.

It automatically aggregates data.

---

# 📥 Load Second Dataset

```python
file_path = os.path.join(
    directory,
    'datasets',
    'pivot_weather_2.csv'
)

df = pd.read_csv(file_path)

print(df.head())

# Output
#        date      city  temperature  humidity
# 0  5/1/2017  new york           65        56
# 1  5/1/2017  new york           61        54
```

---

# 📈 Basic Pivot Table

By default, `pivot_table()` uses the mean aggregation function.

```python
pivot_table_df = df.pivot_table(
    index='date',
    columns='city'
)

print(pivot_table_df)

# Output
#          humidity          temperature
# city       mumbai new york      mumbai new york
# date
# 5/1/2017     81.5     55.0        76.5     63.0
# 5/2/2017     55.5     61.0        81.0     71.0
```

---

# ➕ Pivot Table with Aggregation Function

The `aggfunc` parameter changes the aggregation method.

```python
pivot_table_aggfun_df = df.pivot_table(
    index='date',
    columns='city',
    aggfunc='sum'
)

print(pivot_table_aggfun_df)

# Output
#          humidity          temperature
# city       mumbai new york      mumbai new york
# date
# 5/1/2017      163      110         153      126
# 5/2/2017      111      122         162      142
```

---

# 📑 Pivot Table with Margins

The `margins=True` option adds totals for rows and columns.

```python
pivot_table_margins_df = df.pivot_table(
    index='date',
    columns='city',
    margins=True
)

print(pivot_table_margins_df)

# Output
# Includes row and column totals
```

---

# ⏰ Grouping by Time Using `Grouper`

The `Grouper` class groups datetime data by specific time intervals.

---

# 📅 Convert Date Column

```python
df['date'] = pd.to_datetime(
    df['date']
)
```

---

# 📊 Monthly Grouping

```python
pivot_table_grouper_df = df.pivot_table(
    index=pd.Grouper(
        freq='ME',
        key='date'
    ),
    columns='city'
)

print(pivot_table_grouper_df)

# Output
# Monthly grouped pivot table
```

---

# 🔥 Melting DataFrames Using `melt()`

The `melt()` method converts wide-format data into long-format data.

It is the opposite of pivoting.

---

# 📋 Melt DataFrame

Parameters:

- `id_vars` → Identifier columns
- `value_vars` → Columns to unpivot
- `var_name` → Name for variable column
- `value_name` → Name for value column

```python
melted_df = df.melt(
    id_vars=['date'],
    value_vars=[
        'temperature',
        'humidity'
    ],
    var_name='variable',
    value_name='value'
)

print(melted_df)

# Output
#          date     variable  value
# 0  2017-05-01  temperature     65
# 1  2017-05-01  temperature     61
# 2  2017-05-02  temperature     70
# 3  2017-05-02  temperature     72
```

---

# 🎯 Key Points

- 🔄 `pivot()` reshapes DataFrames
- 📊 `pivot_table()` handles duplicate values
- ➕ `aggfunc` changes aggregation behavior
- 📑 `margins=True` adds totals
- ⏰ `Grouper` groups datetime data
- 🔥 `melt()` converts wide data into long format

---

# ✅ Advantages of Pivoting and Melting

- 📊 Better data organization
- 🔍 Easier data analysis
- 📈 Simplifies reporting
- ⚡ Efficient reshaping operations
- 📑 Creates summary tables quickly
- 🚀 Improves visualization preparation
