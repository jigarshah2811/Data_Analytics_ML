"""

    02b_fetching_rows.py

    The following accesses data by column names instead of index values.

    It then retrieves rows of data from schools.db which has assumed to have been
    created already.  If it has not, run the 01 example in this folder first.

"""
import sqlite3

school_data = []
connection = None
state = input('Schools from which state: ').upper()
try:
    connection = sqlite3.connect('schools.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM schools WHERE state=?', (state,))
    for sch in cursor:
        school_data.append((sch['school_id'], sch['fullname'], sch['city'], sch['state'], sch['country']))
except sqlite3.Error as e:
    print('Error: {0}'.format(e))
finally:
    if connection:
        connection.close()

print('Schools in {0}'.format(state))
for school in school_data:
    print('{name}, {city} {state}'.format(name=school[1], city=school[2], state=school[3]))
