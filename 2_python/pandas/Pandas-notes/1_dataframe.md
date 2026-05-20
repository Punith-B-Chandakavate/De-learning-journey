# 📊 Pandas DataFrame in Python

A **DataFrame** is a 2-dimensional labeled data structure in Pandas.

It is used to store and manipulate tabular data using rows and columns.

---

# 📚 Topics Covered

- 📦 Creating DataFrames
- 📄 Reading CSV Files
- 📏 Working with Rows and Columns
- 📊 Statistical Operations
- 🔍 Selecting Data
- 🗂 Indexing

---

# 📦 Importing Required Modules

The `pandas` library is used for data analysis and manipulation.

The `os` module helps work with file paths.

```python
import os
import pandas as pd
```

---

# 🏗 Creating DataFrame from Dictionary

A DataFrame can be created using a Python dictionary.

Each key becomes a column name.

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df_dict = pd.DataFrame(data)

print(df_dict)

# Output
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston
```

---

# 📄 Creating DataFrame from CSV File

The `read_csv()` method reads data from a CSV file and converts it into a DataFrame.

```python
import os
import pandas as pd

current_dir = os.path.dirname(__file__)

file_path = os.path.join(
    current_dir,
    'datasets',
    'weather_data.csv'
)

df = pd.read_csv(file_path)

print(df)

# Output
#         day  temperature  windspeed event
# 0  1/1/2017           32          6  Rain
# 1  1/2/2017           35          7  Sunny
# 2  1/3/2017           28          2   Snow
# 3  1/4/2017           24          7   Snow
# 4  1/5/2017           32          4  Rain
```

---

# 🔍 Viewing Specific Rows

Slicing is used to display selected rows from the DataFrame.

```python
print(df[2:4])

# Output
#         day  temperature  windspeed event
# 2  1/3/2017           28          2  Snow
# 3  1/4/2017           24          7  Snow
```

---

# 📏 Rows and Columns

The `shape` attribute returns the total number of rows and columns.

- First value → Rows
- Second value → Columns

```python
row, col = df.shape

print(f'Rows: {row}, Columns: {col}')

# Output
# Rows: 5, Columns: 4
```

---

# 📋 DataFrame Information

The `info()` method provides a summary of the DataFrame.

It shows:

- Total rows
- Column names
- Data types
- Memory usage

```python
df.info()

# Output
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
```

---

# 👀 First Rows — `head()`

The `head()` method displays the first rows of the DataFrame.

By default, it returns the first 5 rows.

```python
print(df.head())

# Output
# Displays first 5 rows
```

---

# 👀 Last Rows — `tail()`

The `tail()` method displays the last rows of the DataFrame.

```python
print(df.tail())

# Output
# Displays last 5 rows
```

---

# 👀 Last Row Only

You can pass a number inside `tail()` to display specific rows from the end.

```python
print(df.tail(1))

# Output
#         day  temperature  windspeed event
# 4  1/5/2017           32          4  Rain
```

---

# 🧾 Column Names

The `columns` attribute returns all column names.

```python
print(df.columns)

# Output
# Index(['day', 'temperature', 'windspeed', 'event'], dtype='object')
```

---

# 🌡 Access Single Column

A single column can be accessed using square brackets.

```python
print(df['temperature'])

# Output
# 0    32
# 1    35
# 2    28
# 3    24
# 4    32
```

---

# ⚡ Another Way to Access Column

Columns can also be accessed using dot notation.

```python
print(df.temperature)

# Output
# Same result as above
```

---

# 🧬 Data Types

The `dtypes` attribute shows the data type of each column.

```python
print(df.dtypes)

# Output
# day            object
# temperature     int64
# windspeed       int64
# event          object
```

---

# 📌 Multiple Columns

Multiple columns can be selected using double square brackets.

```python
print(df[['event', 'temperature']])

# Output
#    event  temperature
# 0  Rain           32
# 1 Sunny           35
# 2 Snow           28
# 3 Snow           24
# 4 Rain           32
```

---

# 📊 Minimum and Maximum Values

The `min()` and `max()` methods return the smallest and largest values.

```python
temp = df['temperature']

print('Minimum:', temp.min())
print('Maximum:', temp.max())

# Output
# Minimum: 24
# Maximum: 35
```

---

# 📈 Mean, Median, Standard Deviation

These statistical methods help analyze numerical data.

- `mean()` → Average value
- `median()` → Middle value
- `std()` → Measures variation

```python
print('Mean:', temp.mean())
print('Median:', temp.median())
print('Standard Deviation:', temp.std())

# Output
# Mean: 30.2
# Median: 32.0
# Standard Deviation: 4.6
```

---

# 📑 Summary Statistics — `describe()`

The `describe()` method returns statistical information about numerical columns.

```python
print(df['temperature'].describe())

# Output
# count     5.000000
# mean     30.200000
# std       4.658326
# min      24.000000
# 25%      28.000000
# 50%      32.000000
# 75%      32.000000
# max      35.000000
```

---

# 🔥 Selecting Rows with Conditions

Filtering helps retrieve rows based on conditions.

## 🌡 Temperature Greater Than 30

```python
print(df[df['temperature'] > 30])

# Output
# Rows where temperature > 30
```

---

# 🌧 Event is Rain

Rows can also be filtered using string values.

```python
print(df[df['event'] == 'Rain'])

# Output
# Rows where event is Rain
```

---

# 🏆 Highest Temperature

The `max()` method can be combined with filtering to find rows with the highest value.

```python
print(
    df[df['temperature'] == df['temperature'].max()]
    [['day', 'temperature']]
)

# Output
#         day  temperature
# 1  1/2/2017           35
```

---

# 🗂 Setting Index

The `set_index()` method changes a column into the DataFrame index.

Indexes help access rows quickly.

```python
df.set_index('day', inplace=True)

print(df.loc['1/3/2017'])

# Output
# temperature      28
# windspeed         2
# event          Snow
```

---

# 🔄 Resetting Index

The `reset_index()` method restores the default integer index.

```python
print(df.reset_index())

# Output
# Default integer index restored
```

---

# 📌 Setting Another Index

Different columns can also be used as indexes.

```python
df.set_index('event', inplace=True)

print(df.loc['Snow'])

# Output
# Displays rows where event is Snow
```

---

# 🎯 Key Points

- 📊 DataFrames store tabular data
- 📏 `shape` returns rows and columns
- 👀 `head()` and `tail()` display data
- 📈 Statistical methods analyze data
- 🔍 Filtering retrieves specific rows
- 🗂 `set_index()` changes index
- 🔄 `reset_index()` restores default index

---

# ✅ Advantages of Pandas DataFrame

- ⚡ Fast data analysis
- 📊 Easy data manipulation
- 🔍 Powerful filtering
- 📈 Built-in statistical functions
- 📂 Efficient handling of large datasets