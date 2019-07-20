"""
    task5_1_starter.py  -   Groupby and Pandas

        Using our baseball.csv file, your task was to answer two questions:
            1. Which team has hit the most home runs (cumulative)?
            2. Which team hit the most home runs in 2015?

Then, plot the total home runs hit per decade to see which decade had the most.


"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = '../resources/baseball/Batting.csv'

# Step 1: Use Pandas to read ALL DATA from baseball.csv file into a DataFrame.  Use the
#         first line from the file as the column names.
# baseball = pd.read_csv(filename, delimiter=",", sep=",", header=None,
#             names=['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB',
#                    'CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP'],
#             )

baseball = pd.read_csv(filename)
# Step 2: Check the shape and inspect the info() on the DataFrame
# print("Shape:\n", baseball.shape)
# print("Describe:\n", baseball.describe())
# print("Info:\n", baseball.info(verbose=True))
# print("tail: \n", baseball.tail())

# Step 3: Answer question 1: Which team has hit the most home runs (cumulative)?
#         Hint: Groupby teamID, perform a sum() on the groups, sort by largest HR.

baseball_by_team = baseball[['teamID', 'HR']].groupby(by='teamID').sum()
results = baseball_by_team.sort_values(by='HR', ascending=False)
print(results.index[0])


# Step 4: Answer question 2: Which team hit the most home runs in 2015?
#         Hint: Filter out all records that are not from the yearID 2015, then
#         groupby teamID, perform a sum() on the groups, sort by largest HR.
# Plot HR values
# baseball.get("HR").plot()
# plt.show()
baseball_yr2015 = baseball.loc[baseball['yearID'] == 2015]
baseball_yr2015[['teamID', 'HR']].groupby(by='teamID').sum()
results = baseball_yr2015.sort_values(by='HR', ascending=False)
print(results.iloc[:1])
print(results.iloc[:4]['teamID'])



# Step 5: Define your decade (bins) starting from 1870 going up to 2020.
#         Hint: it's just a list.  : )
bins = np.arange(1870, 2030, 10, dtype=int)

# Step 6: Use Pandas cut() to break the yearID column into decades.  You can create
#         a new column called 'hr_decade' or something similar.
baseball['decade'] = pd.cut(x=baseball['yearID'], bins=bins)


# Step 7: Plot the HRs for each decade as a 'barh' plot.
#         Hint: first groupby 'hr_decade', sum() the groups, then plot only the HR column.
baseball.groupby(by='decade').sum()
baseball.get('HR').plot()
plt.show()
