"""
    1. Grouping data using groupby()
    2. splitting apply
    3. describing groupby objects using describe()

"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Determine the file path dynamically based on the script location
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'datasets', 'weather_data_by_cities.xlsx')
# 1. Grouping data using groupby()
df = pd.read_excel(file_path)
df_grouped = df.groupby('city')
for city, group in df_grouped:
    print(f"City: {city}")
    print(group)
    print("\n")

"""
City: mumbai
        day    city  temperature  windspeed  event_x000d_
4  1/1/2017  mumbai           90          5  Sunny_x000d_
5  1/2/2017  mumbai           85         12    Fog_x000d_
6  1/3/2017  mumbai           87         15    Fog_x000d_
7  1/4/2017  mumbai           92          5   Rain_x000d_


City: new york
        day      city  temperature  windspeed  event_x000d_
0  1/1/2017  new york           32          6   Rain_x000d_
1  1/2/2017  new york           36          7  Sunny_x000d_
2  1/3/2017  new york           28         12   Snow_x000d_
3  1/4/2017  new york           33          7  Sunny_x000d_


City: paris
         day   city  temperature  windspeed   event_x000d_
8   1/1/2017  paris           45         20   Sunny_x000d_
9   1/2/2017  paris           50         13  Cloudy_x000d_
10  1/3/2017  paris           54          8  Cloudy_x000d_
11  1/4/2017  paris           42         10         Cloudy
"""

print('Get group by:\n', df_grouped.get_group('mumbai'))
"""
Get group by:
         day    city  temperature  windspeed  event_x000d_
4  1/1/2017  mumbai           90          5  Sunny_x000d_
5  1/2/2017  mumbai           85         12    Fog_x000d_
6  1/3/2017  mumbai           87         15    Fog_x000d_
7  1/4/2017  mumbai           92          5   Rain_x000d_
"""
print('Max :\n',df_grouped.max())
"""
Max :
                day  temperature  windspeed  event_x000d_
city
mumbai    1/4/2017           92         15  Sunny_x000d_
new york  1/4/2017           36         12  Sunny_x000d_
paris     1/4/2017           54         20  Sunny_x000d_
"""

print('Mean :\n', df_grouped[['temperature', 'windspeed']].mean())
"""
Mean :
           temperature  windspeed
city
mumbai          88.50       9.25
new york        32.25       8.00
paris           47.75      12.75
"""

# 2. splitting apply
df = pd.DataFrame({
    'temperature': ['32 F', '45 KMP', '27 C']
})
df[['value', 'unit']] = df['temperature'].str.split(' ', expand=True)
print('Split :\n', df)
"""
Split :
   temperature value unit
0        32 F    32    F
1      45 KMP    45  KMP
2        27 C    27    C
"""

# 3. describing groupby objects using describe()
print('Describe :\n',df_grouped.describe())
"""
Describe :
          temperature                                                  windspeed
               count   mean       std   min    25%   50%    75%   max     count   mean       std  min   25%   50%    75%   max
city
mumbai           4.0  88.50  3.109126  85.0  86.50  88.5  90.50  92.0       4.0   9.25  5.057997  5.0  5.00   8.5  12.75  15.0
new york         4.0  32.25  3.304038  28.0  31.00  32.5  33.75  36.0       4.0   8.00  2.708013  6.0  6.75   7.0   8.25  12.0
paris            4.0  47.75  5.315073  42.0  44.25  47.5  51.00  54.0       4.0  12.75  5.251984  8.0  9.50  11.5  14.75  20.0
"""
# Visualize the mean temperature by city
df_grouped.plot()

# Visualize the mean temperature by city using a bar plot
df_grouped['temperature'].mean().plot(kind='bar')

# Show plot
plt.show()