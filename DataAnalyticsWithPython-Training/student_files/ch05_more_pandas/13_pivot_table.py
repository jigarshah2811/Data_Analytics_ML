"""

    13_pivot_table.py

"""
import numpy as np
import pandas as pd


data = [[1, 88, 68, 25, 10, 'Sunny', False],
        [2, 84, 65, 31, 5, 'Cloudy', False],
        [3, 86, 66, 32, 5, 'Light Rain', False],
        [4, 89, 67, 26, 5, 'Rain', False],
        [5, 92, 70, 22, 10, 'Sunny', False],
        [6, 95, 71, 18, 20, 'Sunny', True],
        [7, 94, 69, 27, 10, 'Sunny', False],
        [8, 93, 72, 25, 10, 'Rain', False],
        [9, 98, 76, 16, 5,  'Cloudy', True],
        [10, 94, 72, 22, 10, 'Sunny', False]
]


df = pd.DataFrame(data,
                  columns=['Day', 'Highs', 'Lows', 'Humidity', 'Wind Speed', 'Outlook', 'Red Flag'])

df['Outlook'] = df['Outlook'].astype('category')
df['Outlook'].cat.set_categories(['Sunny', 'Rain', 'Light Rain', 'Cloudy'],inplace=True)

pivot = pd.pivot_table(data=df, index=['Outlook'], values=['Highs', 'Lows'], aggfunc=[np.mean, len] )

print(pivot)
print(pivot.query('Outlook == ["Sunny"]'))
pivot.to_excel('sample.xlsx')

print(pd.crosstab(df.Outlook, df['Wind Speed']))