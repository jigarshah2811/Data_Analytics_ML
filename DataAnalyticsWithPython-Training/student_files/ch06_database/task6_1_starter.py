"""
        task 6_1_starter.py     - This task reads from the database using
                                  Pandas APIs to find the maximum baseball salary
                                  ever and the player who earned it.

                                  Your task is to determine the max salary from
                                  the salaries table found in batting.db
                                  by using Pandas idxmax() and then query the
                                  database players table manually to find who's
                                  salary this was and what year it happened.

"""
import pandas as pd
import sqlite3
df = None
df_file = './batting.db'

# Step 1. Use the 'with' control to connect to the database.  Refer to the Pandas example
#         within the student manual on how to do this.  Proper syntax uses the following structure:
#                with <connection_obj> as conn:
#                    do stuff

SQL_SELECT_PLAYER_SALARY_YEAR = "SELECT playerid, salary, year FROM salaries"
SQL_SELECT_PLAYER_NAME = "SELECT playerid, firstname, lastname FROM players"

with sqlite3.connect(df_file) as conn:
    df_players = pd.read_sql(SQL_SELECT_PLAYER_NAME, conn, params=None)
    df_salaries = pd.read_sql(SQL_SELECT_PLAYER_SALARY_YEAR, conn, params=None)


print(df_players.shape)
print(df_players.info)
print(df_salaries.shape)
print(df_salaries.info)

maxSalaryIndex = df_salaries['salary'].idxmax()
maxSalary = df_salaries['salary'][maxSalaryIndex]
yearForMaxSalary = df_salaries['year'][maxSalaryIndex]
playerIdForMaxSalary = df_salaries['playerid'][maxSalaryIndex]

print("maxSalary: {0}\n, yearForMaxSalary: {1}\n, playerIdForMaxSalary:{2}\n".format(maxSalary, yearForMaxSalary, playerIdForMaxSalary))


# Step 2. Use read_sql() twice to read from BOTH tables within the 'with' control
#         The following sql should work for both:
#                   SELECT playerid, salary, year FROM salaries
#                   SELECT playerid, firstname, lastname FROM players


# Step 3. Once you have the loaded the DataFrames, get the index for the max salary value
#         using idx_max = df['salary'].idxmax()
#         Take this resulting idx_max value, plug it back into the salary column.  It should look something like this:
#                                       max_salary = df['salary'][idx_max]

#         The values for the other two columns might look something like this:
#                                       year_for_max_salary = df['year'][idx_max]
#                                       playerid = df['playerid'][idx_max]


# Step 4. Use the playerid obtained from step 3 to find the firstname and lastname of the
#         that playerid
record = df_players[df_players['playerid'] == playerIdForMaxSalary]
print(record.firstname.values[0], record.lastname.values[0])

record = df_salaries[df_salaries['playerid'] == playerIdForMaxSalary]
print(record)

print(df_salaries.sort_values(by='salary', ascending=False).iloc[0].playerid)
# Step 5. Display the player's name, salary, and year for that salary.

# MERGE approach
merged = pd.merge(df_players, df_salaries, on='playerid')
id = merged['salary'].idxmax()
maxSalary = merged['salary'][id]
record = merged[merged.salary == maxSalary]
print(record)
print(merged.salary.max())