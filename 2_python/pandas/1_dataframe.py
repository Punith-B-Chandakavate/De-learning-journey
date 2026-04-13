'''
    Topic: DataFrame
    1. Creating a DataFrame from a dictionary and excel file
    2. Dealing with rows and columns
    3. Operations: min, max, mean, median, std
    4. Concatenation selecting data
    5. set_index, reset_index
'''
import os
import pandas as pd
# 1. Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df_dict = pd.DataFrame(data)
print(df_dict)

# 1. Creating a DataFrame from an excel file
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'datasets', 'weather_data.csv')
    
df = pd.read_csv(file_path)
print(df)
# view the 2nd to 4th rows of the DataFrame.
print(df[2:4])

# 2. Dealing with rows and columns
# print rows and columns
row, col = df.shape
print(f'Rows: {row}, Columns: {col}')

# print information about the DataFrame.
df.info()

# print the first 5 rows of the DataFrame.
print(df.head())

# print the last 5 rows of the DataFrame.
print(df.tail())
print(df.tail(1))

# print the column names of the DataFrame.
print(df.columns)

# print the column data = of the 'Temperature' column.
print(df['temperature'])
print(df.temperature)

# print the data types of each column in the DataFrame.
print(df.dtypes)
print(type(df.temperature))

# print the columns 'event' and 'temperature'.
print(df[['event', 'temperature']])

# 3. Operations: min, max, mean, median, std
# print the minimum and maximum value of the 'temperature' column.
temp = df['temperature']
print('Minimum temperature:', temp.min())
print('Maximum temperature:', temp.max())

# print the mean, median, and standard deviation of the 'temperature' column.
print('Mean(Average Value) temperature:', temp.mean())
print('Median(Middle Value) temperature:', temp.median())
print('Standard deviation(+/-) of temperature:', temp.std())

# print a summary of statistics for the 'temperature' column.
print('\nSummary statistics for temperature:')
print(df['temperature'].describe())

# 4. Concatenation selecting data
# Get all rows where the temperature is greater than 30 degrees.
print(df[df['temperature'] > 30])

# Get all rows where the event is 'Rain'.
print(df[df['event'] == 'Rain'])

# Get the day(s) with the highest temperature.
print(df[df['temperature'] == df['temperature'].max()][['day', 'temperature']])

# 5. set_index, reset_index
# Set the 'day' column as the index of the DataFrame.
print(df.set_index('day', inplace=True))
print(df.loc['1/3/2017'])


# Reset the index back to the default integer index.
print(df.set_index('day').reset_index())
print(df.reindex(inplace=True))

# Set the 'event' column as the index of the DataFrame.
print(df.set_index('event', inplace=True))

# view the row for the event 'Snow'.
print(df.loc['Snow'])