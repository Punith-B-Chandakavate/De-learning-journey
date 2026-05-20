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
"""
Original DataFrame:
        date      city  temperature  humidity
0  5/1/2017  new york           65        56
1  5/1/2017  new york           61        54
2  5/2/2017  new york           70        60
3  5/2/2017  new york           72        62
4  5/1/2017    mumbai           75        80
5  5/1/2017    mumbai           78        83
6  5/2/2017    mumbai           82        85
7  5/2/2017    mumbai           80        26
"""

# Pivoting DataFrames using pd.pivot_table() is similar to pivot() but it can handle duplicate values for one index/column pair. 
# By default, it will aggregate the duplicate values using the mean function, but you can specify other aggregation functions as well.
pivot_table_df = df.pivot_table(index='date', columns='city')
print('Pivot Table DataFrame:\n', pivot_table_df)
"""

Pivot Table DataFrame:
          humidity          temperature
city       mumbai new york      mumbai new york
date
5/1/2017     81.5     55.0        76.5     63.0
5/2/2017     55.5     61.0        81.0     71.0
"""

pivot_table_aggfun_df = df.pivot_table(index='date', columns='city', aggfunc='sum')
print('Pivot Table DataFrame:\n', pivot_table_aggfun_df)
"""
Pivot Table DataFrame:
          humidity          temperature
city       mumbai new york      mumbai new york
date
5/1/2017      163      110         153      126
5/2/2017      111      122         162      142
"""

# You can also add margins to the pivot table to get the totals for rows and columns.
pivot_table_margins_df = df.pivot_table(index='date', columns='city', margins=True)
print('Pivot Table DataFrame with margins:\n', pivot_table_margins_df)
"""
Pivot Table DataFrame with margins:
          humidity                 temperature
city       mumbai new york    All      mumbai new york     All
date
5/1/2017     81.5     55.0  68.25       76.50     63.0  69.750
5/2/2017     55.5     61.0  58.25       81.00     71.0  76.000
All          68.5     58.0  63.25       78.75     67.0  72.875
"""

df['date'] = pd.to_datetime(df['date'])
# You can also use a Grouper to group by a specific time period, such as month or year.
pivot_table_grouper_df = df.pivot_table(index=pd.Grouper(freq='ME', key='date'), columns='city')
print('Pivot Table DataFrame with grouper:\n', pivot_table_grouper_df)
"""
Pivot Table DataFrame with grouper:
            humidity          temperature
city         mumbai new york      mumbai new york
date
2017-05-31     68.5     58.0       78.75     67.0
"""


# 3. Melting DataFrames using pd.melt()
# Melting is the inverse of pivoting. It transforms a DataFrame from a wide format to a long format.
# id_vars: column(s) to use as identifier variables.
# value_vars: column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.
# var_name: name to use for the ‘variable’ column. If None it uses ‘variable’.
# value_name: name to use for the ‘value’ column. If None it uses ‘value’.
melted_df = df.melt(id_vars=['date'], value_vars=['temperature', 'humidity'], var_name='variable', value_name='value')
print('Melted DataFrame:\n', melted_df)
"""
Melted DataFrame:
          date     variable     value
0  2017-05-01         city  new york
1  2017-05-01         city  new york
2  2017-05-02         city  new york
3  2017-05-02         city  new york
4  2017-05-01         city    mumbai
5  2017-05-01         city    mumbai
6  2017-05-02         city    mumbai
7  2017-05-02         city    mumbai
8  2017-05-01  temperature        65
9  2017-05-01  temperature        61
10 2017-05-02  temperature        70
11 2017-05-02  temperature        72
12 2017-05-01  temperature        75
13 2017-05-01  temperature        78
14 2017-05-02  temperature        82
15 2017-05-02  temperature        80
16 2017-05-01     humidity        56
17 2017-05-01     humidity        54
18 2017-05-02     humidity        60
19 2017-05-02     humidity        62
20 2017-05-01     humidity        80
21 2017-05-01     humidity        83
22 2017-05-02     humidity        85
23 2017-05-02     humidity        26
"""