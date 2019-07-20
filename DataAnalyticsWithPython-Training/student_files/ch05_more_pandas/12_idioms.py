"""

        12_idioms.py -

"""
import numpy as np
import pandas as pd

# our starting DataFrame
df = pd.DataFrame(data=np.arange(1, 10).reshape((3, 3)), columns=['first', 'second', 'third'])
print(df)


# Splitting a Frame
print('\nsplitting a frame:')
criterion = (df['first'] < 4)
df_new = df[criterion]
df_new2 = df[~criterion]
print(df_new)
print(df_new2)


# Membership
print('\nmembership:')
print(df[df.index.isin([0, 1]) & df['second'].isin([1, 2, 3])])



# Complement
print('\ncomplement:')
print(df[~(df.index.isin([0, 1]) & df['second'].isin([1, 2, 3]))])



# Assigning a value to a column based on a condition from another
print('\nassigning a value to a column based on a criterion from another column:')
df.loc[df['second'] >= 5, 'third'] = -1
print(df)



# A new DataFrame
data = [
    ['Dick Cabbage', 'Tulsa'],
    ['Tina Turnip', 'Oklahoma City'],
    ['Elvis Parsley', 'Tulsa'],
    ['Antonio Banana', 'Norman'],
    ['Howie Mango', 'Oklahoma City'],
    ['Tom Shanks', 'Norman'],
    ['Tom Shanks', 'Norman']
]
df2 = pd.DataFrame(data=data, columns=['name', 'city'])
print(df2)

# finding the first of each group...
city_groups = df2.groupby('city')
print('\nfind the first of each group:')
print(city_groups.first().reset_index())

print(city_groups.nth(1))                           # without resetting the index, the city becomes the index, nth(1) gets second item of each group
print(city_groups.first().loc['Norman'])
