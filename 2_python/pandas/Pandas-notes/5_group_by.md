# 📊 GroupBy Operations in Pandas

The `groupby()` method in Pandas is used to group data based on one or more columns.

It helps perform:

- 📊 Aggregation
- 🔍 Data analysis
- 📈 Statistical summaries
- 🧩 Split-Apply-Combine operations

---

# 📚 Topics Covered

- 📦 Grouping data using `groupby()`
- ✂ Split and Apply operations
- 📑 Describing grouped data
- 📊 Data visualization

---

# 📦 Importing Required Modules

The `pandas` library is used for data analysis.

The `matplotlib` library is used for visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt
import os
```

---

# 📁 Load Excel Dataset

The Excel file is loaded dynamically using the current script directory.

```python
directory = os.path.dirname(
    os.path.abspath(__file__)
)

file_path = os.path.join(
    directory,
    'datasets',
    'weather_data_by_cities.xlsx'
)

df = pd.read_excel(file_path)

print(df.head())

# Output
#         day      city  temperature  windspeed   event
# 0  1/1/2017  new york           32          6   Rain
# 1  1/2/2017  new york           36          7  Sunny
```

---

# 📦 Grouping Data Using `groupby()`

The `groupby()` method groups rows with the same values together.

```python
df_grouped = df.groupby('city')

for city, group in df_grouped:

    print(f"City: {city}")

    print(group)

# Output
# City: mumbai
# City: new york
# City: paris
```

---

# 🔍 Access Specific Group

The `get_group()` method retrieves data for a specific group.

```python
print(
    df_grouped.get_group('mumbai')
)

# Output
#         day    city  temperature  windspeed  event
# 4  1/1/2017  mumbai           90          5  Sunny
# 5  1/2/2017  mumbai           85         12    Fog
```

---

# 📈 Maximum Values in Each Group

The `max()` method returns the highest value from each group.

```python
print(df_grouped.max())

# Output
#            temperature  windspeed
# city
# mumbai              92         15
# new york            36         12
# paris               54         20
```

---

# 📊 Mean Values in Each Group

The `mean()` method calculates the average values.

```python
print(
    df_grouped[
        ['temperature', 'windspeed']
    ].mean()
)

# Output
#            temperature  windspeed
# city
# mumbai           88.50       9.25
# new york         32.25       8.00
# paris            47.75      12.75
```

---

# ✂ Split and Apply Operation

The `split()` operation divides strings into multiple columns.

---

# 🌡 Split Temperature and Unit

The `str.split()` method splits string values.

```python
df = pd.DataFrame({
    'temperature': [
        '32 F',
        '45 KMP',
        '27 C'
    ]
})

df[['value', 'unit']] = (
    df['temperature']
    .str.split(' ', expand=True)
)

print(df)

# Output
#   temperature value unit
# 0        32 F    32    F
# 1      45 KMP    45  KMP
# 2        27 C    27    C
```

---

# 📑 Describe Grouped Data

The `describe()` method provides statistical summaries for grouped data.

It returns:

- Count
- Mean
- Standard deviation
- Minimum value
- Maximum value
- Quartiles

```python
print(
    df_grouped.describe()
)

# Output
# Statistical summary of grouped data
```

---

# 📊 Plot Grouped Data

Pandas provides built-in plotting support using Matplotlib.

```python
df_grouped.plot()

# Output
# Line plots for grouped data
```

---

# 📉 Bar Plot of Mean Temperature

A bar chart can visualize average temperature by city.

```python
df_grouped[
    'temperature'
].mean().plot(kind='bar')

plt.show()

# Output
# Bar chart displaying mean temperature
```

---

# 🎯 Key Points

- 📦 `groupby()` groups similar data
- 🔍 `get_group()` retrieves specific groups
- 📈 `max()` finds maximum values
- 📊 `mean()` calculates averages
- ✂ `split()` separates string data
- 📑 `describe()` gives statistical summaries
- 📉 `plot()` visualizes grouped data

---

# ✅ Advantages of GroupBy Operations

- 📊 Easy data summarization
- 🚀 Faster data analysis
- 📈 Better statistical insights
- 🔍 Simplifies grouped calculations
- 📉 Built-in visualization support
- ⚡ Efficient for large datasets