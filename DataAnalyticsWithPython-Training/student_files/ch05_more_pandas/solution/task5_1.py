"""
    task5_1.py  -   Groupby and Pandas
"""
import os

import matplotlib.pyplot as plt
import pandas as pd


filename = '../../resources/baseball/Batting.csv'
batting = pd.read_csv(filename)
print('{0} shape: {1}'.format(os.path.basename(filename), batting.shape))

print(batting.info())

most_hrs = batting.groupby('teamID').sum().sort_values('HR', ascending=False)
print(most_hrs.head())
print('Question 1 answer: {0}'.format(most_hrs.index[0]))

hrs_2015 = batting[batting['yearID'] == 2015].groupby('teamID').sum().sort_values('HR', ascending=False)
print(hrs_2015.head())
print('Question 2 answer: {0}'.format(hrs_2015.index[0]))

bins = [1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
# or use bins=range(1870, 2030, 10)

batting['hr_decade'] = pd.cut(batting['yearID'], bins=bins)
batting.groupby('hr_decade').sum()['HR'].plot(kind='barh')
plt.show()