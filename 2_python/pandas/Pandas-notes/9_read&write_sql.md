# 📚 Stack, Unstack, and Crosstab in Pandas

Pandas provides advanced reshaping and summarization functions to organize and analyze data efficiently.

These operations are useful for:

- 🔄 Reshaping DataFrames
- 📊 Multi-level indexing
- 📈 Data summarization
- 🔍 Frequency analysis

---

# 📚 Topics Covered

- 📦 `stack()` — Convert columns into rows
- 🔄 `unstack()` — Convert rows back into columns
- 📊 `crosstab()` — Frequency tables and summaries

---

# 📦 Importing Required Modules

The `pandas` library is used for data manipulation.

```python
import pandas as pd
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
    'stock.xlsx'
)

df = pd.read_excel(
    file_path,
    header=[0, 1]
)

print(df.head())

# Output
#   Unnamed: 0_level_0    Price
#             Company Facebook Google
# 0          05-Jun-17      155    955
# 1          06-Jun-17      150    987
```

---

# 📦 `stack()` — Stack Columns into Rows

The `stack()` method converts columns into rows.

It creates a multi-level index.

---

# 🔄 Basic Stack Operation

```python
stack_df = df.stack()

print(stack_df)

# Output
#                    Price
# 0 Facebook         155
#   Google           955
# 1 Facebook         150
#   Google           987
```

---

# 📊 Stack with Specific Level

The `level` parameter specifies which column level to stack.

```python
stack_df_2 = df.stack(level=0)

print(stack_df_2)

# Output
# Multi-level stacked DataFrame
```

---

# 🔄 `unstack()` — Convert Rows Back into Columns

The `unstack()` method reverses the stacking process.

It converts row indexes back into columns.

```python
unstack_df = stack_df.unstack()

print(unstack_df)

# Output
# Original DataFrame restored
```

---

# 📚 Three-Level Header DataFrame

Pandas can also work with DataFrames having multiple header levels.

---

# 📥 Read Excel with 3-Level Header

```python
file_path = os.path.join(
    directory,
    'datasets',
    'stock_3_level.xlsx'
)

df_l3 = pd.read_excel(
    file_path,
    header=[0, 1, 2]
)

print(df_l3.head())

# Output
# DataFrame with 3-level columns
```

---

# 🔄 Stack Three-Level DataFrame

```python
stack_l3_df = df_l3.stack(level=2)

print(stack_l3_df)

# Output
# Stacked 3-level DataFrame
```

---

# 📊 `crosstab()` — Frequency Table

The `crosstab()` method calculates the frequency of combinations between columns.

It is commonly used for categorical analysis.

---

# 📥 Load Survey Dataset

```python
file_path = os.path.join(
    directory,
    'datasets',
    'survey.xlsx'
)

df_crosstab = pd.read_excel(file_path)

print(df_crosstab.head())

# Output
#     Name Nationality     Sex
# 0  Kathy         USA  Female
# 1  Linda         USA  Female
```

---

# 📈 Basic Crosstab

This counts combinations between two columns.

```python
cross_tab = pd.crosstab(
    df_crosstab.Nationality,
    df_crosstab.Sex
)

print(cross_tab)

# Output
# Sex          Female  Male
# Nationality
# Bangadesh         1     1
# China             2     1
# India             0     3
# USA               2     2
```

---

# ➕ Crosstab with Totals and Percentages

Parameters:

- `margins=True` → Adds totals
- `normalize=True` → Converts counts into percentages

```python
cross_tab_2 = pd.crosstab(
    df_crosstab.Nationality,
    df_crosstab.Sex,
    margins=True,
    normalize=True
)

print(cross_tab_2)

# Output
# Crosstab with totals and percentages
```

---

# 📊 Multi-Level Crosstab

Multiple columns can be used together.

```python
cross_tab_3 = pd.crosstab(
    [
        df_crosstab.Nationality,
        df_crosstab.Sex
    ],
    [
        df_crosstab.Handedness_x000d_
    ],
    margins=True
)

print(cross_tab_3)

# Output
# Multi-level crosstab
```

---

# 📈 Crosstab with Aggregation Function

The `values` and `aggfunc` parameters allow statistical calculations.

---

# 📊 Average Age by Nationality and Gender

```python
import numpy as np

cross_tab_4 = pd.crosstab(
    df_crosstab.Nationality,
    df_crosstab.Sex,
    values=df_crosstab.Age,
    aggfunc=np.average
)

print(cross_tab_4)

# Output
# Sex          Female       Male
# Nationality
# Bangadesh      31.0  25.000000
# China          55.0  43.000000
# India           NaN  34.333333
# USA            20.5  20.500000
```

---

# 🎯 Key Points

- 📦 `stack()` converts columns into rows
- 🔄 `unstack()` restores columns
- 📊 `crosstab()` creates frequency tables
- ➕ `margins=True` adds totals
- 📈 `normalize=True` calculates percentages
- 📚 Multi-level indexing supports complex datasets
- ⚡ Aggregation functions provide statistical summaries

---

# ✅ Advantages of Stack, Unstack, and Crosstab

- 📊 Better data organization
- 🔍 Easy categorical analysis
- 📈 Simplifies reporting
- ⚡ Efficient reshaping operations
- 📑 Supports multi-level indexing
- 🚀 Useful for statistical analysis
