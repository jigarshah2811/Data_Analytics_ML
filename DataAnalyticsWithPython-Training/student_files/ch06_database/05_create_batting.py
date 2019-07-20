import csv
import sqlite3

data_sourcefile1 = '../resources/baseball/Batting.csv'
data_sourcefile2 = '../resources/baseball/Salaries.csv'
data_sourcefile3 = '../resources/baseball/Master.csv'

DROP_TABLE1 = 'DROP TABLE IF EXISTS batting'
DROP_TABLE2 = 'DROP TABLE IF EXISTS salaries'
DROP_TABLE3 = 'DROP TABLE IF EXISTS players'

CREATE_TABLE1 = 'CREATE TABLE IF NOT EXISTS batting (playerid VARCHAR(50), year INTEGER, hits INTEGER, atbats INTEGER)'
INSERT_RECORD1 = 'INSERT INTO batting(playerid, year, hits, atbats) VALUES (?,?,?,?)'

CREATE_TABLE2 = 'CREATE TABLE IF NOT EXISTS salaries (year INTEGER, team VARCHAR(10), league VARCHAR(10), playerid VARCHAR(50), salary INTEGER)'
INSERT_RECORD2 = 'INSERT INTO salaries(year, team, league, playerid, salary) VALUES (?,?,?,?,?)'

CREATE_TABLE3 = 'CREATE TABLE IF NOT EXISTS players (playerid VARCHAR(50), firstname VARCHAR(40), lastname VARCHAR(40))'
INSERT_RECORD3 = 'INSERT INTO players(playerid, firstname, lastname) VALUES (?,?,?)'

# read data from the file into a list of records
data1, data2, data3 = [], [], []
try:
    with open(data_sourcefile1, encoding='utf8') as f1, \
         open(data_sourcefile2, encoding='utf8') as f2, \
         open(data_sourcefile3, encoding='utf8') as f3:
        try:
            for row in csv.reader(f1):
                try:
                    atbats = int(row[6])
                    hits = int(row[8])
                    year = int(row[1])
                    data1.append((row[0], year, hits, atbats))
                except ValueError:
                    pass

            for row in csv.reader(f2):
                try:
                    row[0] = int(row[0])
                    team = row[1]
                    league = row[2]
                    playerid = row[3]
                    row[4] = int(row[4])
                    data2.append(row)
                except ValueError:
                    pass

            for row in csv.reader(f3):
                try:
                    data3.append((row[0], row[13], row[14]))
                except ValueError:
                    pass

        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)

print('read {0} records from Batting.csv'.format(len(data1)))
print('read {0} records from Salaries.csv'.format(len(data2)))
print('read {0} records from Master.csv'.format(len(data3)))

print('Connecting to database...')
with sqlite3.connect('batting.db') as connection:
    print('Preparing to create tables...')
    cursor = connection.cursor()
    print('Preparing to load data into batting table')
    cursor.execute(DROP_TABLE1)
    cursor.execute(CREATE_TABLE1)
    cursor.executemany(INSERT_RECORD1, data1)
    print('Data loaded into batting table')
    print('Preparing to load data into salaries table')
    cursor.execute(DROP_TABLE2)
    cursor.execute(CREATE_TABLE2)
    cursor.executemany(INSERT_RECORD2, data2)
    print('Data loaded into salaries table')
    print('Preparing to load data into players table')
    cursor.execute(DROP_TABLE3)
    cursor.execute(CREATE_TABLE3)
    cursor.executemany(INSERT_RECORD3, data3)
    print('Data loaded into players table')
print('Database setup finished.')
