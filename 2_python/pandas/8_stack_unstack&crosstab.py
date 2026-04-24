"""
    1. stack - to stack the columns of a DataFrame into a single column, creating a multi-level index
    2. unstack - to unstack a stacked DataFrame
    3. crosstab - to get the count of each combination of two columns
"""
import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory,'datasets', 'stock.xlsx')

df = pd.read_excel(file_path, header=[0,1])
print('DataFrame:\n', df)
"""
DataFrame:
   Unnamed: 0_level_0    Price                  Price to earnings ratio (P/E)                 _x000d_
             Company Facebook Google Microsoft                      Facebook Google Microsoft_x000d_
0          05-Jun-17      155    955        66                         37.10   32.0     30.31_x000d_
1          06-Jun-17      150    987        69                         36.98   31.3     30.56_x000d_
2          07-Jun-17      153    963        62                         36.78   31.7     30.46_x000d_
3          08-Jun-17      155   1000        61                         36.11   31.2     30.11_x000d_
4          09-Jun-17      156   1012        66                         37.07   30.0        31_x000d_
"""
# stack the DataFrame
stack_df = df.stack()
print('stack data:\n', stack_df)
"""
stack data:
                    Unnamed: 0_level_0   Price  Price to earnings ratio (P/E)       _x000d_
0 Company                   05-Jun-17     NaN                            NaN           NaN
  Facebook                        NaN   155.0                          37.10           NaN
  Google                          NaN   955.0                          32.00           NaN
  Microsoft                       NaN    66.0                            NaN           NaN
1 Company                   06-Jun-17     NaN                            NaN           NaN
  Facebook                        NaN   150.0                          36.98           NaN
  Google                          NaN   987.0                          31.30           NaN
  Microsoft                       NaN    69.0                            NaN           NaN
2 Company                   07-Jun-17     NaN                            NaN           NaN
  Facebook                        NaN   153.0                          36.78           NaN
  Google                          NaN   963.0                          31.70           NaN
  Microsoft                       NaN    62.0                            NaN           NaN
3 Company                   08-Jun-17     NaN                            NaN           NaN
  Facebook                        NaN   155.0                          36.11           NaN
  Google                          NaN  1000.0                          31.20           NaN
  Microsoft                       NaN    61.0                            NaN           NaN
4 Company                   09-Jun-17     NaN                            NaN           NaN
  Facebook                        NaN   156.0                          37.07           NaN
  Google                          NaN  1012.0                          30.00           NaN
  Microsoft                       NaN    66.0                            NaN           NaN
"""

# stack with level parameter to specify the level to stack
stack_df_2 = df.stack(level=0)
print('stack DataFrame: \n',  stack_df_2)
"""
stack DataFrame: for level=0
                                    Company  Facebook  Google  Microsoft Microsoft_x000d_
0 Unnamed: 0_level_0             05-Jun-17       NaN     NaN        NaN              NaN
  Price                                NaN    155.00   955.0       66.0              NaN
  Price to earnings ratio (P/E)        NaN     37.10    32.0        NaN              NaN
1 Unnamed: 0_level_0             06-Jun-17       NaN     NaN        NaN              NaN
  Price                                NaN    150.00   987.0       69.0              NaN
  Price to earnings ratio (P/E)        NaN     36.98    31.3        NaN              NaN
2 Unnamed: 0_level_0             07-Jun-17       NaN     NaN        NaN              NaN
  Price                                NaN    153.00   963.0       62.0              NaN
  Price to earnings ratio (P/E)        NaN     36.78    31.7        NaN              NaN
3 Unnamed: 0_level_0             08-Jun-17       NaN     NaN        NaN              NaN
  Price                                NaN    155.00  1000.0       61.0              NaN
  Price to earnings ratio (P/E)        NaN     36.11    31.2        NaN              NaN
4 Unnamed: 0_level_0             09-Jun-17       NaN     NaN        NaN              NaN
  Price                                NaN    156.00  1012.0       66.0              NaN
  Price to earnings ratio (P/E)        NaN     37.07    30.0        NaN              NaN
"""

# unstack the stacked DataFrame
unstack_df = stack_df.unstack()
print('Unstack DataFrame:\n', unstack_df)
"""
Unstack DataFrame:
   Unnamed: 0_level_0    Price                  Price to earnings ratio (P/E)                
             Company Facebook Google Microsoft                      Facebook Google Microsoft
0          05-Jun-17      155    955        66                         37.10   32.0     30.31
1          06-Jun-17      150    987        69                         36.98   31.3     30.56
2          07-Jun-17      153    963        62                         36.78   31.7     30.46
3          08-Jun-17      155   1000        61                         36.11   31.2     30.11
4          09-Jun-17      156   1012        66                         37.07   30.0        31
"""

file_path = os.path.join(directory,'datasets', 'stock_3_level.xlsx')

# read excel file with 3 level header
df_l3 = pd.read_excel(file_path, header=[0, 1, 2])
print('DataFrame:\n', df_l3)

# stack with level parameter to specify the level to stack
stack_l3_df = df_l3.stack(level=2)
print('Stack L3 DataFrame:\n', stack_l3_df)

# 3. Crosstab - to get the count of each combination of two columns
file_path = os.path.join(directory, 'datasets', 'survey.xlsx')
df_crosstab = pd.read_excel(file_path)
print('Crosstab DataFrame:\n', df_crosstab)
"""
Crosstab DataFrame:
      Name Nationality     Sex  Age Handedness_x000d_
0    Kathy         USA  Female   23      Right_x000d_
1    Linda         USA  Female   18      Right_x000d_
2    Peter         USA    Male   19      Right_x000d_
3     John         USA    Male   22       Left_x000d_
4   Fatima   Bangadesh  Female   31       Left_x000d_
5    Kadir   Bangadesh    Male   25       Left_x000d_
6   Dhaval       India    Male   35       Left_x000d_
7   Sudhir       India    Male   31       Left_x000d_
8   Parvir       India    Male   37      Right_x000d_
9      Yan       China  Female   52      Right_x000d_
10    Juan       China  Female   58       Left_x000d_
11   Liang       China    Male   43       Left_x000d_
"""

# crosstab to get the count of each combination of two columns
cross_tab = pd.crosstab(df_crosstab.Nationality, df_crosstab.Sex)
print('cross tab:\n', cross_tab)
"""
cross tab:
 Sex          Female  Male
Nationality
Bangadesh         1     1
China             2     1
India             0     3
USA               2     2
"""

# with margins parameter to get the total count of each row and column
# margins parameter to get the total count of each row and column 
# normalize parameter to get the percentage of each combination of two columns
cross_tab_2 = pd.crosstab(df_crosstab.Nationality, df_crosstab.Sex, margins=True, normalize=True)
print('cross tab 2:\n', cross_tab_2)
"""
cross tab 2:
 Sex          Female  Male  All
Nationality
Bangadesh         1     1    2
China             2     1    3
India             0     3    3
USA               2     2    4
All               5     7   12
"""
cross_tab_3 = pd.crosstab([df_crosstab.Nationality, df_crosstab.Sex], [df_crosstab.Handedness_x000d_], margins=True)
print('cross tab 3:\n', cross_tab_3)
"""
cross tab 3:
 Handedness_x000d_   Left_x000d_  Right_x000d_  All
Nationality Sex                                   
Bangadesh   Female            1             0    1
            Male              1             0    1
China       Female            1             1    2
            Male              1             0    1
India       Male              2             1    3
USA         Female            0             2    2
            Male              1             1    2
All                           7             5   12
"""
import numpy as np

# crosstab with values and aggfunc parameters to get the average age of each combination of two columns
cross_tab_4 = pd.crosstab(df_crosstab.Nationality, df_crosstab.Sex, values=df_crosstab.Age, aggfunc=np.average)
print('cross tab 4:\n', cross_tab_4)
"""
cross tab 4:
 Sex          Female       Male
Nationality                   
Bangadesh      31.0  25.000000
China          55.0  43.000000
India           NaN  34.333333
USA            20.5  20.500000
"""