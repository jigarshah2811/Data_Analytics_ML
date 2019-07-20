import pandas as pd
import sqlite3
df = pd.DataFrame()

with sqlite3.connect('batting.db') as conn:
    df = pd.read_sql('SELECT hits, atbats FROM batting WHERE year >= ?', conn, params=['1957'])
    print('Dataframe shape: {0}'.format(df.shape))

df = df[df.atbats >= 502]

df['averages'] = df['hits'] / df['atbats']

print(df.describe())
print('50% batting average: {0:.3f}'.format(df.describe()['averages']['50%']))
