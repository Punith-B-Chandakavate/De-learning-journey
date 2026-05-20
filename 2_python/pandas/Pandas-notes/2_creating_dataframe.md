# 📊Create a DataFrame in Pandas

A **DataFrame** is a 2-dimensional data structure in Pandas used to store data in rows and columns.

Pandas provides multiple ways to create DataFrames depending on the data source.

---

# 📚 Topics Covered

- 📄 Creating DataFrame from CSV File
- 📗 Creating DataFrame from Excel File
- 📦 Creating DataFrame from Dictionary
- 📋 Creating DataFrame from List of Tuples
- 🧾 Creating DataFrame from List of Dictionaries

---

# 📦 Importing Required Modules

The `pandas` library is used for creating and managing DataFrames.

The `os` module helps work with file paths.

```python
import pandas as pd
import os
```

---

# 📄 Creating DataFrame from CSV File

The `read_csv()` method reads data from a CSV file and converts it into a DataFrame.

```python
import pandas as pd
import os

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
# 1  1/2/2017           35          7 Sunny
# 2  1/3/2017           28          2  Snow
# 3  1/4/2017           24          7  Snow
# 4  1/5/2017           32          4  Rain
```

---

# 📗 Creating DataFrame from Excel File

The `read_excel()` method reads Excel files and converts them into a DataFrame.

You can also specify a sheet name.

```python
import pandas as pd
import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(
    current_dir,
    'datasets',
    'weather_data.xlsx'
)

# Read default sheet
df = pd.read_excel(file_path)

# Read specific sheet
df = pd.read_excel(
    file_path,
    sheet_name='Sheet1'
)

print(df)

# Output
#         day  temperature  windspeed event
# 0  1/1/2017           32          6  Rain
# 1  1/2/2017           35          7 Sunny
# 2  1/3/2017           28          2  Snow
# 3  1/4/2017           24          7  Snow
# 4  1/5/2017           32          4  Rain
```

---

# 📦 Creating DataFrame from Dictionary

A Python dictionary can be converted into a DataFrame.

Each key becomes a column name.

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

print(df)

# Output
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston
```

---

# 📋 Creating DataFrame from List of Tuples

A list of tuples can also be converted into a DataFrame.

Column names must be specified manually.

```python
import pandas as pd

data = [
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 35, 'Chicago'),
    ('David', 40, 'Houston')
]

df = pd.DataFrame(
    data,
    columns=['Name', 'Age', 'City']
)

print(df)

# Output
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston
```

---

# 🧾 Creating DataFrame from List of Dictionaries

Each dictionary represents a row in the DataFrame.

Keys become column names.

```python
import pandas as pd

data = [
    {
        'Name': 'Alice',
        'Age': 25,
        'City': 'New York'
    },
    {
        'Name': 'Bob',
        'Age': 30,
        'City': 'Los Angeles'
    },
    {
        'Name': 'Charlie',
        'Age': 35,
        'City': 'Chicago'
    },
    {
        'Name': 'David',
        'Age': 40,
        'City': 'Houston'
    }
]

df = pd.DataFrame(data)

print(df)

# Output
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston
```

---

# 🎯 Key Points

- 📊 DataFrames store data in tabular format
- 📄 `read_csv()` reads CSV files
- 📗 `read_excel()` reads Excel files
- 📦 Dictionaries can create DataFrames
- 📋 Tuples require column names
- 🧾 List of dictionaries creates row-wise data

---

# ✅ Advantages of DataFrames

- ⚡ Fast data processing
- 📊 Easy data analysis
- 🔍 Powerful filtering and selection
- 📈 Built-in statistical functions
- 📂 Supports multiple data sources
- 🚀 Efficient handling of large datasets
