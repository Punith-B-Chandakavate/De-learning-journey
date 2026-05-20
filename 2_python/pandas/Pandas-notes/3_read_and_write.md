# 📂 Pandas File Handling Guide

Pandas provides powerful functions to read, write, and manage files such as CSV and Excel files.

This guide demonstrates:

- 📄 Reading CSV files
- ✍ Writing CSV files
- 📗 Reading Excel files
- 🧹 Cleaning data while reading
- 📤 Writing Excel files
- 📑 Creating multiple Excel sheets

---

# 📦 Importing Required Modules

The `pandas` library is used for file handling and data analysis.

The `os` module helps work with file paths.

```python
import pandas as pd
import os
```

---

# 📁 Get Current Directory

The current file directory is useful for working with relative paths.

```python
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

print(BASE_DIR)

# Output
# Current project directory path
```

---

# 📄 CSV File Handling

CSV (Comma-Separated Values) files are widely used to store tabular data.

---

# 📥 Read CSV File

The `read_csv()` method reads CSV files into a DataFrame.

```python
file_path = os.path.join(
    BASE_DIR,
    'datasets',
    'stock_data.csv'
)

df = pd.read_csv(file_path)

print(df.head())

# Output
#   tickers   eps  revenue  price    people
# 0    AAPL  5.61   365.82  150.2  Tim Cook
# 1   GOOGL  4.56   257.64 2800.5 Sundar Pichai
```

---

# ⏭ Skip Rows While Reading CSV

The `skiprows` parameter skips rows from the beginning.

```python
df_skip = pd.read_csv(
    file_path,
    skiprows=1
)

print(df_skip.head())

# Output
# CSV data after skipping first row
```

---

# 🧾 Use Specific Row as Header

The `header` parameter defines which row should be used as column names.

```python
df_header = pd.read_csv(
    file_path,
    header=1
)

print(df_header.head())

# Output
# Data using second row as header
```

---

# 🏷 Custom Column Names

You can manually assign column names if the file has no header.

```python
df_custom = pd.read_csv(
    file_path,
    header=None,
    names=[
        'tickers',
        'eps',
        'revenue',
        'price',
        'people'
    ]
)

print(df_custom.head())

# Output
# DataFrame with custom column names
```

---

# 🔢 Read Limited Rows

The `nrows` parameter limits how many rows are read.

```python
df_limited = pd.read_csv(
    file_path,
    nrows=3
)

print(df_limited)

# Output
# First 3 rows only
```

---

# 🧹 Handle Missing Values Globally

The `na_values` parameter converts invalid values into `NaN`.

```python
df_na = pd.read_csv(
    file_path,
    na_values=['n.a.', 'not available']
)

print(df_na)

# Output
# Invalid values converted to NaN
```

---

# 🎯 Handle Missing Values Per Column

Different columns can have different missing value rules.

```python
df_column_na = pd.read_csv(
    file_path,
    na_values={
        'eps': ['n.a.', 'not available'],
        'revenue': ['n.a.', 'not available', -1],
        'people': ['n.a.', 'not available', -1]
    }
)

print(df_column_na)

# Output
# Column-specific missing values handled
```

---

# ✍ Export DataFrame to CSV

The `to_csv()` method exports a DataFrame into a CSV file.

```python
export_path = os.path.join(
    BASE_DIR,
    'datasets',
    'stock_data_output.csv'
)

df.to_csv(export_path, index=False)

print("CSV file exported successfully")

# Output
# CSV file exported successfully
```

---

# 📌 Export Selected Columns

Only selected columns can be exported.

```python
df.to_csv(
    export_path,
    index=False,
    columns=['tickers', 'eps', 'revenue']
)

print("Selected columns exported")

# Output
# Selected columns exported
```

---

# 🚫 Export CSV Without Header

The `header=False` option removes column names.

```python
df.to_csv(
    export_path,
    index=False,
    header=False
)

print("CSV exported without header")

# Output
# CSV exported without header
```

---

# 📗 Excel File Handling

Pandas can also read and write Excel files easily.

---

# 📥 Read Excel File

The `read_excel()` method reads Excel files into a DataFrame.

```python
file_path = os.path.join(
    BASE_DIR,
    'datasets',
    'stock_data.xlsx'
)

df = pd.read_excel(
    file_path,
    sheet_name='Sheet1'
)

print(df.head())

# Output
# Excel data loaded successfully
```

---

# 🧹 Data Cleaning Using Converters

Converters allow cleaning data while reading Excel files.

---

# 👤 Convert Invalid Names

```python
def convert_people(cell):

    if cell == 'n.a.':
        return 'Sam Walton'

    return cell
```

---

# 📊 Convert Invalid EPS Values

```python
def convert_eps(cell):

    if cell == 'not available':
        return None

    return cell
```

---

# ⚡ Read Excel with Converters

The `converters` parameter applies custom cleaning functions.

```python
df_cleaned = pd.read_excel(
    file_path,
    sheet_name='Sheet1',
    converters={
        'people': convert_people,
        'eps': convert_eps
    }
)

print(df_cleaned)

# Output
# Cleaned Excel data
```

---

# ✍ Export DataFrame to Excel

The `to_excel()` method writes data into an Excel file.

```python
export_path = os.path.join(
    BASE_DIR,
    'datasets',
    'stock_data_output.xlsx'
)

df_cleaned.to_excel(
    export_path,
    index=False
)

print("Excel file exported")

# Output
# Excel file exported
```

---

# 📌 Write Excel Starting from Specific Row and Column

The `startrow` and `startcol` parameters define where writing begins.

```python
df_cleaned.to_excel(
    export_path,
    sheet_name='Sheet2',
    index=False,
    startrow=1,
    startcol=2
)

print("Excel written at custom position")

# Output
# Excel written at custom position
```

---

# 📑 Writing Multiple Sheets in One Excel File

The `ExcelWriter()` class allows writing multiple DataFrames into different sheets.

---

# 📊 Sample Stock Data

```python
df_stock = pd.DataFrame({
    'tickers': ['AAPL', 'GOOGL', 'AMZN'],
    'eps': [5.61, 4.56, 3.45]
})

print(df_stock)

# Output
#   tickers   eps
# 0    AAPL  5.61
# 1   GOOGL  4.56
# 2    AMZN  3.45
```

---

# 🌦 Sample Weather Data

```python
df_weather = pd.DataFrame({
    'city': ['New York', 'Chicago'],
    'temperature': [75, 70]
})

print(df_weather)

# Output
#        city  temperature
# 0  New York           75
# 1   Chicago           70
```

---

# 📤 Export Multiple Sheets

```python
export_path = os.path.join(
    BASE_DIR,
    'datasets',
    'combined_data.xlsx'
)

with pd.ExcelWriter(export_path) as writer:

    df_stock.to_excel(
        writer,
        sheet_name='Stock Data',
        index=False
    )

    df_weather.to_excel(
        writer,
        sheet_name='Weather Data',
        index=False
    )

print("Multiple sheets written successfully")

# Output
# Multiple sheets written successfully
```

---

# 🎯 Key Points

- 📄 `read_csv()` reads CSV files
- 📗 `read_excel()` reads Excel files
- 🧹 `na_values` handles missing values
- ⚡ `converters` clean data while reading
- ✍ `to_csv()` exports CSV files
- 📤 `to_excel()` exports Excel files
- 📑 `ExcelWriter()` creates multiple sheets

---

# ✅ Advantages of Pandas File Handling

- ⚡ Fast file processing
- 📊 Easy data manipulation
- 🧹 Built-in data cleaning
- 📂 Supports CSV and Excel files
- 📈 Efficient for large datasets
- 🚀 Simplifies data workflows
