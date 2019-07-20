#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os


# In[5]:


arr = np.array([1, 2, 3])
print(arr)
os.getcwd()


# This is MarkDown block with Escape+M 
# 
# # This is header
# #### This is sub-header 

# In[23]:


# Create numpy array
arr1 = np.array([
            [1, 2, 3],
            [1, 2],
])
arr1
type(arr1)


# In[13]:


# Find shape of array
arr3 = np.array( [
        [1, 2, 3],
        [1, 2],
] )

arr3
arr3.shape #Shows the shape, (Axis0 len, Axis1 len)


# In[32]:


# Type of array
arr3 = np.array( [
        [1, 2, 3],
        [1, 2, 3],
] , dtype=float
)

arr3
print(type(arr3))
print(arr3.dtype)

arr3.shape # Shows the shape, (Axis0 len, Axis1 len)


# In[38]:


# Type cast type of array
arr_new = arr3.astype(np.float64)
print (arr_new)
print (arr_new.dtype)


# In[48]:


# Create array with 0s
arr4 = np.zeros((2, 2))
print(arr4)
arr5 = np.ones((2, 2))
print(arr5)


# In[41]:


# Create array with increments
arr6 = np.linspace(0, 20, 5) # (Start, End, Increment)
arr6


# In[ ]:


# Create array with range (STEP)
arr7 = np.arange(start, end, step)


# In[42]:


# Create diagonal array
arr_diag = np.diag(np.arange(1, 6, 2)) # (Start, End, Increment)
arr_diag


# In[50]:


# Combinining Arrays
result = np.column_stack([arr4, arr5])
print(result)

result = np.vstack([arr4, arr5])
print(result)

# Shifting / rollover
np.roll(arr3, 1, axis=0)
np.roll(arr3, 1, axis=1)


# In[ ]:




