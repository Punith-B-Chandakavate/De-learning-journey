"""
    1. fillna() - Fill missing values with a specified value or method
    2. dropna() - Drop rows or columns with missing values
    3. isna() / notna() - Detect missing values
    4. interpolate() - Fill missing values using interpolation
    5. replace() - Replace specific values (including missing value indicators)

"""

import pandas as pd
import os

# Determine the file path dynamically based on the script location
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'datasets', 'weather_data_1.csv')

# Read the CSV file and parse the 'day' column as datetime
df = pd.read_csv(file_path, parse_dates=['day'])

# Set the 'day' column as the index
df.set_index('day', inplace=True)

# ------------- Handle missing values by filling them -------------
# Fill all missing values with 0
df = df.fillna(0)

# Alternatively, fill specific columns with appropriate values
df = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'No Event'
})

# Forward fill: propagate the last valid value forward
df = df.ffill()

# Backward fill: fill using the next valid value
df = df.bfill()


# ------------- Drop rows with missing values (if needed) ------------- 
# Drop rows that contain any missing values
df = df.dropna()

# Drop rows where all values are missing
df = df.dropna(how='all')

# Keep only rows with at least 2 non-missing values
df = df.dropna(thresh=2)

# Drop rows where 'temperature' is missing
df = df.dropna(subset=['temperature'])


# ------------- Detect missing values -------------
# Create a boolean DataFrame indicating missing values
missing_mask = df.isna()

# Create a boolean DataFrame indicating non-missing values
not_missing_mask = df.notna()


# ------------- Interpolate missing numeric values -------------
# Perform linear interpolation on numeric columns
df[['temperature', 'windspeed']] = df[['temperature', 'windspeed']].interpolate()

# Perform time-based interpolation using the datetime index
df[['temperature', 'windspeed']] = df[['temperature', 'windspeed']].interpolate(method='time')


# ------------- Replace specific values -------------

# Replace string 'NaN' with actual pandas NA value
df = df.replace('NaN', pd.NA)
df = df.replace(-9999, pd.NA)
df = df.replace([-9999, -8888], pd.NA)

# Replace NA values with the string 'Missing'
df = df.replace({pd.NA: 'Missing'})
df = df.replace({
    'temperature': {pd.NA: 'Missing'},
    'windspeed': {pd.NA: 'Missing'},
    'event': {pd.NA: 'Missing'}
})

df = df.replace({
    'temperature': -9999,
    'windspeed': -9999,
    'event': 0
}, pd.NA)


# ------ replace NaN using numpy's np.nan ------
import numpy as np
df.replace(-9999, np.nan)
df.replace([-9999, -8888], np.nan)
df.replace({
    'temperature': -9999,
    'windspeed': -9999,
    'event': 0
}, np.nan)
df.replace({
    -9999: np.nan,
    "No Event": "Missing"
})

# --- replace using regex ---
# Remove all alphabetic characters from the DataFrame
df = df.replace(r'[A-Za-z]+', '', regex=True) 

# Remove all alphabetic characters from 'temperature' and 'windspeed' columns
df = df.replace({
    'temperature': r'[A-Za-z]+',
    'windspeed': r'[A-Za-z]+',
}, "", regex=True) 

# Replace specific string values with numeric scores
df = pd.DataFrame({
    "score": ["excellent", "good", "average", "poor", "excellent"],
    "student": ["Alice", "Bob", "Charlie", "David", "Eve"]
})
df = df.replace(["excellent", "good", "average", "poor"], [4, 3, 2, 1])
print(df)
