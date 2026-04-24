"""
    1. DateTimeIndex - to work with time series data in pandas
    2. Resampling - to change the frequency of time series data
"""
from matplotlib import pyplot as plt
import pandas as pd
import os

import os

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(directory, 'datasets', 'aapl.csv')

# 1. DateTimeIndex - to work with time series data in pandas
df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
df = df.sort_index()
print('DataFrame:\n', df.head(4))
print('DataFrame Index:\n', df.index)

print('Data for January 2017:\n', df.loc['2017-01'])
print('Data for January 2017:\n', df.loc['2017-01-03':'2017-01-05'])


# 2. Resampling - to change the frequency of time series data
monthly_df = df.Close.resample('ME').mean()
print('Monthly Resampled DataFrame:\n', monthly_df)
"""
Monthly Resampled DataFrame:
 Date
2016-07-31     99.473333
2016-08-31    107.665217
2016-09-30    110.857143
2016-10-31    115.707143
2016-11-30    110.154286
2016-12-31    114.335714
2017-01-31    119.570000
2017-02-28    133.713684
2017-03-31    140.617826
2017-04-30    142.886842
2017-05-31    152.227727
2017-06-30    147.831364
"""

monthly_df = df.Close.resample('ME').mean().plot(kind='line', title='Monthly Resampled DataFrame')
plt.show()