"""
    Different ways to create a DataFrame in pandas.
    1. using CSV file
    2. Using a Excel file
    3. Using a dictionary
    4. Using a list of tuples
    5. Using a list of dictionaries
"""

import pandas as pd
import os

current_dir = os.path.dirname(__file__)

# 1. Creating a DataFrame from a CSV file
file_path = os.path.join(current_dir, 'datasets', 'weather_data.csv')
df = pd.read_csv(file_path) # read the CSV file into a DataFrame

# 2. Creating a DataFrame from an Excel file
file_path = os.path.join(current_dir, 'datasets', 'weather_data.xlsx')
df = pd.read_excel(file_path) # read the excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name='Sheet1') # specify the sheet name if there are multiple sheets in the excel file


# 3. Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data) # create a DataFrame from the dictionary

# 4. Creating a DataFrame from a list of tuples
data = [
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 35, 'Chicago'),
    ('David', 40, 'Houston')
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City']) # create a DataFrame from the list of tuples and specify the column names

# 5. Creating a DataFrame from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},      
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
    {'Name': 'David', 'Age': 40, 'City': 'Houston'}
]
df = pd.DataFrame(data) # create a DataFrame from the list of dictionaries



print(df)
