"""
        task 3_1_starter.py     - scatter plot the batting averages from the
                                  previous exercise against atbats

"""
import matplotlib.pyplot as plt
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

data = np.genfromtxt('../resources/baseball/Batting.csv', skip_header=1,
                     usecols=(1, 6, 8), delimiter=',', dtype=float)
print("Read from file, now shape: ", data.shape)

data = data[data[:, 1] >= 502]
print("Filtered Column with record atBats < 502, now shape: ", data.shape)

data = data[data[:, 0] >= 1957]
print("Filtered column with record year >= 1957, now shape: ", data.shape)

avgs = data[:, 2] / data[:, 1]
data = np.column_stack([data, avgs])
print("Stacked Avg column: now shape: ", data.shape)



data = data[data[:, 3].argsort()]
print("Sorted by Avg column: now shape: ", data.shape)

print(data[-1:-100:-1, 3])


# add your plot code here, note: you may opt to use your task2_2_starter.py
# solution instead.

# Step 1. Create a figure and add axes.  set_xlabel() and set_ylabel()
avgs = data[:, 3]
atbats = data[:, 1]

figure = plt.figure(figsize=(12, 6), facecolor="#ccee77")
ax = figure.add_axes((0.1, 0.1, 0.8, 0.8), facecolor="#f0fdfd")


x = avgs
y = atbats
plt.scatter(x, y, marker=".", c="#f08327")
plt.show()

# Step 2. Invoke scatter() from the figure.

# Step 3. Create a legend and annotate the maximum value.

# Step 4. Show the plot.
