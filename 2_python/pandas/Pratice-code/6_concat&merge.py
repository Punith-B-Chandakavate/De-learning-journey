"""
    1. Concatenating DataFrames using pd.concat()
    2. Merging DataFrames using pd.merge()

"""

# ----------------- Concatenating DataFrames using pd.concat() -----------------
import pandas as pd

india_weather = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 27],
    'humidity': [80, 60, 78]
})

us_weather = pd.DataFrame({
    'city': ['new york', 'chicago', 'orlando'],
    'temperature': [21, 14, 35],
    'humidity': [68, 65, 75]
})


# Concatenate DataFrames row-wise (default) and ignore_index=True will reset the index in the resulting DataFrame.
df = pd.concat([india_weather, us_weather], ignore_index=True)
"""
Concatenated DataFrame:
         city  temperature  humidity
0     mumbai           32        80
1      delhi           45        60
2  bangalore           27        78
3   new york           21        68
4    chicago           14        65
5    orlando           35        75
"""

# Concatenate DataFrames with keys to create a hierarchical index in the resulting DataFrame. The keys will be used to label the rows from each DataFrame in the resulting DataFrame.
df = pd.concat([india_weather, us_weather], keys=['india', 'us'])
print('Concatenated DataFrame:\n', df)
"""
Concatenated DataFrame:
               city  temperature  humidity
india 0     mumbai           32        80
      1      delhi           45        60
      2  bangalore           27        78
us    0   new york           21        68
      1    chicago           14        65
      2    orlando           35        75
"""

print('India Weather:\n', df.loc['india'])
print('US Weather:\n', df.loc['us'])
"""
India Weather:
         city  temperature  humidity
0     mumbai           32        80
1      delhi           45        60
2  bangalore           27        78
US Weather:
        city  temperature  humidity
0  new york           21        68
1   chicago           14        65
2   orlando           35        75
"""


# Concatenate DataFrames with different columns
temperature_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 27]
}, index=[0, 1, 2])

windspeed_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'windspeed': [7, 12, 9]
}, index=[0, 1, 2])

# axis=0 -> row-wise concatenation (default) and axis=1 -> column-wise concatenation
df = pd.concat([temperature_df, windspeed_df], axis=1)
print('Concatenated DataFrame:\n', df)
""""
Concatenated DataFrame:
         city  temperature       city  windspeed
0     mumbai           32     mumbai          7
1      delhi           45      delhi         12
2  bangalore           27  bangalore          9
"""
# Concatenate Series with DataFrame (series will be added as a new column)
s = pd.Series(["humid", "dry", "rainy"], name="event")
df = pd.concat([temperature_df, s], axis=1) 
print('Concatenated DataFrame:\n', df)
"""
Concatenated DataFrame:
         city  temperature  event
0     mumbai           32  humid
1      delhi           45    dry
2  bangalore           27  rainy
"""

# ----------------- Merging DataFrames using pd.merge() -----------------
df1 = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore', 'chennai'],
    'temperature': [32, 45, 27, 30]
})

df2 = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'windspeed': [7, 12, 9]
})

# By default, merge performs an inner join, which means it will only include rows with matching values in the 'city' column from both DataFrames.
df = pd.merge(df1, df2, on='city')
print('Inner Join:\n', df)
"""
Inner Join:
         city  temperature  windspeed
0     mumbai           32          7
1      delhi           45         12
2  bangalore           27          9
"""

# If you want to include all rows from both DataFrames, you can specify the type of join using the 'how' parameter (e.g., 'outer', 'left', 'right').

# The left join will include all rows from the left DataFrame (df1) and the matching rows from the right DataFrame (df2). If there is no match, the result will contain NaN for the columns from the right DataFrame.
df_left = pd.merge(df1, df2, on='city', how='left')
print('Left Join:\n', df_left)
"""
Left Join:
         city  temperature  windspeed
0     mumbai           32        7.0
1      delhi           45       12.0
2  bangalore           27        9.0
3    chennai           30        NaN
"""

# The right join will include all rows from the right DataFrame (df2) and the matching rows from the left DataFrame (df1). If there is no match, the result will contain NaN for the columns from the left DataFrame.
df_right = pd.merge(df1, df2, on='city', how='right')
print('Right Join:\n', df_right)
"""
Right Join:
         city  temperature  windspeed
0     mumbai           32          7
1      delhi           45         12
2  bangalore           27          9
"""

# The outer join will include all rows from both DataFrames. If there is no match, the result will contain NaN for the columns from the DataFrame that does not have a match.
df_outer = pd.merge(df1, df2, on='city', how='outer', indicator=True)
print('Outer Join:\n', df_outer)
"""
Outer Join:
         city  temperature  windspeed     _merge
0  bangalore           27        9.0       both
1    chennai           30        NaN  left_only
2      delhi           45       12.0       both
3     mumbai           32        7.0       both
"""


# If both DataFrames have columns with the same name (other than the key column), you can use the 'suffixes' parameter to specify suffixes for the overlapping column names in the resulting DataFrame.
df_1 = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 27],
    'humidity': [80, 60, 78]
})
df_2 = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [30, 40, 25],
    'humidity': [7, 12, 9]
})
df_3 = pd.merge(df_1, df_2, on='city', suffixes=('_left', '_right'))
print('Merge Result:\n', df_3)
""""
Merge Result:
         city  temperature_left  humidity_left  temperature_right  humidity_right
0     mumbai                32             80                 30               7
1      delhi                45             60                 40              12
2  bangalore                27             78                 25               9
"""
