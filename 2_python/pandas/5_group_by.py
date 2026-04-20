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

print(df_grouped.get_group('mumbai'))
print(df_grouped.max())
print(df_grouped[['temperature', 'windspeed']].mean())

# 2. splitting apply
df = pd.DataFrame({
    'temperature': ['32 F', '45 KMP', '27 C']
})
df[['value', 'unit']] = df['temperature'].str.split(' ', expand=True)
print(df)

# 3. describing groupby objects using describe()
print(df_grouped.describe())

# Visualize the mean temperature by city
df_grouped.plot()

# Visualize the mean temperature by city using a bar plot
df_grouped['temperature'].mean().plot(kind='bar')

# Show plot
plt.show()