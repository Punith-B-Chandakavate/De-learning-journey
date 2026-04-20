"""
    1. Pivoting DataFrames using pd.pivot()
    2. Pivoting DataFrames using pd.pivot_table()
    3. melting DataFrames using pd.melt()

"""

import pandas as pd
import os

# Determine the file path dynamically based on the script location
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'datasets', 'pivot_weather_1.csv')
# Read the CSV file
df = pd.read_csv(file_path)
print('Original DataFrame:\n', df)


# 1. Pivoting DataFrames using pd.pivot()
# index: column to use to make new frame’s index. 
# columns: column to use to make new frame’s columns. 
# values: column(s) to use for populating new frame’s values.
pivot_df = df.pivot(index='date', columns='city')
print('Pivoted DataFrame:\n', pivot_df)
"""
Pivoted DataFrame:
          temperature                 humidity
city         beijing mumbai new york  beijing mumbai new york
date
5/1/2017          80     75       65       26     80       56
5/2/2017          77     78       66       30     83       58
5/3/2017          79     82       68       35     85       60
"""

pivot_df = df.pivot(index='date', columns='city', values='temperature')

print('Pivoted DataFrame with temperature values:\n', pivot_df)
"""
Pivoted DataFrame:
 city      beijing  mumbai  new york
date
5/1/2017       80      75        65
5/2/2017       77      78        66
5/3/2017       79      82        68
"""


# 2. Pivoting DataFrames using pd.pivot_table()
file_path = os.path.join(directory, 'datasets', 'pivot_weather_2.csv')
# Read the CSV file
df = pd.read_csv(file_path)
print('Original DataFrame:\n', df)

# Pivoting DataFrames using pd.pivot_table() is similar to pivot() but it can handle duplicate values for one index/column pair. 
# By default, it will aggregate the duplicate values using the mean function, but you can specify other aggregation functions as well.
pivot_table_df = df.pivot_table(index='date', columns='city')
print('Pivot Table DataFrame:\n', pivot_table_df)

pivot_table_aggfun_df = df.pivot_table(index='date', columns='city', aggfunc='sum')
print('Pivot Table DataFrame:\n', pivot_table_aggfun_df)

# You can also add margins to the pivot table to get the totals for rows and columns.
pivot_table_margins_df = df.pivot_table(index='date', columns='city', margins=True)
print('Pivot Table DataFrame with margins:\n', pivot_table_margins_df)

df['date'] = pd.to_datetime(df['date'])
# You can also use a Grouper to group by a specific time period, such as month or year.
pivot_table_grouper_df = df.pivot_table(index=pd.Grouper(freq='ME', key='date'), columns='city')
print('Pivot Table DataFrame with grouper:\n', pivot_table_grouper_df)


# 3. Melting DataFrames using pd.melt()
# Melting is the inverse of pivoting. It transforms a DataFrame from a wide format to a long format.
# id_vars: column(s) to use as identifier variables.
# value_vars: column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.
# var_name: name to use for the ‘variable’ column. If None it uses ‘variable’.
# value_name: name to use for the ‘value’ column. If None it uses ‘value’.
melted_df = df.melt(id_vars=['date'], value_vars=['temperature', 'humidity'], var_name='variable', value_name='value')
print('Melted DataFrame:\n', melted_df)