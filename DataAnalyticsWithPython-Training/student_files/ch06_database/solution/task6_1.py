import pandas as pd
import sqlite3

df = None
db_file = '../batting.db'
conn = None

try:
    with sqlite3.connect(db_file) as conn:
        salaries = pd.read_sql('SELECT playerid, salary, year FROM salaries', conn)
        players  = pd.read_sql('SELECT playerid, firstname, lastname FROM players', conn)
finally:
    if conn:
        print('Connection closed!')
        conn.close()

print(salaries.shape)
print(salaries.head())

print(players.shape)
print(players.head())

idx = salaries.salary.idxmax()
playerid = salaries.playerid[idx]
salary = salaries.salary[idx]
year = salaries.year[idx]

highest_paid = players.loc[players.playerid == playerid, ['firstname', 'lastname']]
print(highest_paid)

name = highest_paid.values.squeeze()
print(name)

print('{0} {1} made ${2:,} in {3}'.format(name[0], name[1], salary, year))
