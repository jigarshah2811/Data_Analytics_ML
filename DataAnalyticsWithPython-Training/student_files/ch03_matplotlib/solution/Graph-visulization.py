#!/usr/bin/env python
# coding: utf-8

# In[19]:


"""
        task 3_1_starter.py     - scatter plot the batting averages from the
                                  previous exercise against atbats

"""
import matplotlib.pyplot as plt
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

data = np.genfromtxt('Batting.csv', skip_header=1,
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



# In[20]:


inx_for_max = data[:, 3].argmax()
max_avg = data[inx_for_max, 3]
atbats_for_max_avg = data[inx_for_max, 1]
max_avg, atbats_for_max_avg


# In[21]:


# add your plot code here, note: you may opt to use your task2_2_starter.py
# solution instead.

# Step 1. Create a figure and add axes.  set_xlabel() and set_ylabel()


figure = plt.figure(figsize=(12, 6), facecolor="#ccee77")
ax = figure.add_axes((0.1, 0.1, 0.8, 0.8), facecolor="#f0fdfd")


# Step 2. Invoke scatter() from the figure.

# Step 3. Create a legend and annotate the maximum value.

# Step 4. Show the plot.

ax.set_xlabel('Batting Averge')
ax.set_ylabel('At Bats')

avgs = data[:, 3]
atbats = data[:, 1]
x = avgs
y = atbats

# plt.scatter(x, y, marker=".", c="#f08327") # Simple method to plot graph
ax.scatter(x, y, marker='.', c="#f08327")

ax.legend(['At bats'], loc='best')
ax.annotate(xy=(max_avg, atbats_for_max_avg), s=f'Max={max_avg: .3f}', arrowprops=dict())


# In[ ]:




