"""

    02_fetching_rows.py

    The following source will create a namedtuple called School.

    It then retrieves rows of data from schools.db which has assumed to have been
    created already.  If it has not, run the 01 example in this folder first.

"""
import sqlite3

school_data = []
connection = None
state = input('Schools from which state: ').upper()
try:
    connection = sqlite3.connect('schools.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM schools WHERE state=?', (state,))
    for sch in cursor:
        school_data.append((sch[0], sch[1], sch[2], sch[3], sch[4]))
        # school_data.append(sch)
except sqlite3.Error as e:
    print('Error: {0}'.format(e))
finally:
    if connection:
        connection.close()

print('Schools in {0}'.format(state))
for school in school_data:
    print('{name}, {city} {state}'.format(name=school[1], city=school[2],
                                          state=school[3]))
