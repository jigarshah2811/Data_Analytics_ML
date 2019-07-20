#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np

# Create NumPy Array with different types of values
weather = np.array([
        [0, 88, 68, 25, 10, "Sunny", False],
        [0, 84, 65, 25, 10, "Cloudy", False],
        [0, 86, 66, 25, 10, "Light Rain", False],
        [0, 89, 67, 25, 10, "Rain", False],
        [0, 92, 70, 25, 10, "Sunny", False],
        [0, 95, 71, 25, 10, "Sunny", True],
        [0, 94, 69, 25, 10, "Sunny", False],
], dtype=object)

print(weather)

# shape , size , strides , and number of dimensions
weather.shape
weather.size
weather.ndim


# In[20]:



# Select  col=1 and col=2 from all rows
tempratures  = weather[:, (1,2)]
# tempratures  = weather[::2, (1,2)] # Every alternative Days!
# tempratures = weather[0:5,(1, 3)] # 5 rows, col 1 and 3
tempratures


# In[21]:


# Get average, Col wise!
arr2 = np.average(tempratures, axis=1)
arr2


# In[22]:


# Get average of everything
np.mean(arr2)


# In[32]:


# Filtering: Get all entries with more then 90 temp
high_weather = weather[:, 1]
print(high_weather)
mask =  high_weather >= 90
high_weather[mask]


no_nans = weather[~np.isnan(weather).any(axis=1)]    # Filter out NaN values
no_infs = weather[~np.isinf(data).any(axis=1)]                 # Filter out inf values


# In[33]:


# SORTING: Sort by high temp

high_weather[high_weather.argsort()]


# In[ ]:




