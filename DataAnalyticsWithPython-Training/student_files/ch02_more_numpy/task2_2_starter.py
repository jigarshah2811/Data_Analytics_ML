"""
        task 2_2_starter.py - retrieve the top 100 batting averages from the provided source file:
                                <student_files>/resources/baseball/Batting.csv

                            - remove any rows where the 'atbats' was less than 502 (the official statistic).

"""
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

# Step 1. Read from the file.  Identify the delimiter.  We need columns 6 & 8 from the file.
#         You should also skip the first line.
data = np.genfromtxt('../resources/baseball/Batting.csv',
                     delimiter=",",
                     usecols=(1,6,8),
                     skip_header=1,
                     dtype=int
                     )
# Year, AtBats, hits
#===================
print("Read from file, now shape: ", data.shape)

# Step 2. Remove any rows with atbats that are less than 502.  Hint, use:
#                    results = results[column >= 502]
atBats = data[:, 1]
mask = atBats >= 502
data = data[mask]
print("Filtered Column with record atBats < 502, now shape: ", data.shape)



# Step 3. Remove any rows for the year earlier than 1957.  Hint, use:
#                    results = results[column >= 1957]
year = data[:, 0]
mask = year >= 1957
data = data[mask]
print("Filtered column with record year >= 1957, now shape: ", data.shape)



# Step 4. Calculate the averages.


#         Join the hits, atbats, and averages columns together.  You can use several
#         techniques.  column_stack() might be the most straight forward.

avg = data[:, 2] / data[:, 1]
data = np.column_stack([data, avg])
print("Stacked Avg column: now shape: ", data.shape)

# Step 5. Use the argsort() technique shown in the slides to sort the data
#         based on the averages column.
data = sort_by_avg = data[data[:, 3].argsort()]
print("Sorted by Avg column: now shape: ", data.shape)


# Step 6. Display the final values.
print(data[-1:-100:-1, 3])