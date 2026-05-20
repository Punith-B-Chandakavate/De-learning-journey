"""
PANDAS FILE HANDLING GUIDE
--------------------------
This script demonstrates how to:
1. Read CSV files in different ways
2. Write CSV files
3. Read Excel files (with data cleaning)
4. Write Excel files
5. Write multiple sheets in one Excel file
"""

import pandas as pd
import os


# Get current file directory (useful for relative paths)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------- CSV SECTION ---------------- #

"""Examples of reading and writing CSV files"""

file_path = os.path.join(BASE_DIR, 'datasets', 'stock_data.csv')

# Basic CSV read
df = pd.read_csv(file_path)

# Skip first row
df_skip = pd.read_csv(file_path, skiprows=1)

# Use second row as header
df_header = pd.read_csv(file_path, header=1)

# Assign custom column names (when no header exists)
df_custom = pd.read_csv(
    file_path,
    header=None,
    names=['tickers', 'eps', 'revenue', 'price', 'people']
)

# Read only first 3 rows
df_limited = pd.read_csv(file_path, nrows=3)

# Handle missing values globally
df_na = pd.read_csv(
    file_path,
    na_values=['n.a.', 'not available']
)

# Handle missing values per column
df_column_na = pd.read_csv(
    file_path,
    na_values={
        'eps': ['n.a.', 'not available'],
        'revenue': ['n.a.', 'not available', -1],
        'people': ['n.a.', 'not available', -1],
    }
)

# Export CSV
export_path = os.path.join(BASE_DIR, 'datasets', 'stock_data_output.csv')

# Write full DataFrame
df.to_csv(export_path, index=False)

# Write selected columns only
df.to_csv(export_path, index=False, columns=['tickers', 'eps', 'revenue'])

# Write without header
df.to_csv(export_path, index=False, header=False)




# ---------------- EXCEL SECTION ---------------- #

def convert_people(cell):
    """Custom cleaning: replace 'n.a.' with a name"""
    if cell == 'n.a.':
        return 'Sam Walton'
    return cell


def convert_eps(cell):
    """Custom cleaning: replace invalid values with None"""
    if cell == 'not available':
        return None
    return cell


"""Examples of reading and writing Excel files"""

file_path = os.path.join(BASE_DIR, 'datasets', 'stock_data.xlsx')

# Read Excel normally
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Read Excel with converters (data cleaning while reading)
df_cleaned = pd.read_excel(
    file_path,
    sheet_name="Sheet1",
    converters={
        'people': convert_people,
        'eps': convert_eps
    }
)

# Export Excel
export_path = os.path.join(BASE_DIR, 'datasets', 'stock_data_output.xlsx')

# Write basic Excel
df_cleaned.to_excel(export_path, index=False)

# Write starting from specific row/column
df_cleaned.to_excel(
    export_path,
    sheet_name='Sheet2',
    index=False,
    startrow=1,
    startcol=2
)

# ---------------- MULTIPLE SHEETS ---------------- #

"""Write multiple DataFrames into one Excel file"""

# Sample stock data
df_stock = pd.DataFrame({
    'tickers': ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'META'],
    'eps': [5.61, 4.56, 3.45, 6.78, 2.34],
    'revenue': [365.82, 257.64, 469.82, 168.09, 117.93],
    'price': [150.25, 2800.50, 3400.75, 300.10, 350.20],
    'people': ['Tim Cook', 'Sundar Pichai', 'Andy Jassy', 'Satya Nadella', 'Mark Zuckerberg']
})

# Sample weather data
df_weather = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'temperature': [75, 85, 70, 90, 105],
    'humidity': [60, 50, 65, 70, 20]
})

export_path = os.path.join(BASE_DIR, 'datasets', 'combined_data.xlsx')

# Write both DataFrames into different sheets
with pd.ExcelWriter(export_path) as writer:
    df_stock.to_excel(writer, sheet_name='Stock Data', index=False)
    df_weather.to_excel(writer, sheet_name='Weather Data', index=False)

