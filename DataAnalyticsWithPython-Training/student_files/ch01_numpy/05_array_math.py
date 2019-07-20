import numpy as np

arr22 = np.array([[1, 2], [3, 4]])
arr23 = np.array([[5, 6], [7, 8]])

arr24 = arr22 + arr23                       # [[6  8]
                                            #  [10 12]]
print(arr24)


arr26 = arr22 - arr23                       # [[0. 2. 3.][4. 4. 6.][7. 8. 8.]]
print(arr26)


arr27 = arr22 * arr23                       # same as np.multiply(arr1, arr2)
print(arr27)                                # [[1. 0. 0.][0. 5. 0.][0. 0. 9.]]


a = b = np.array([1, 2, 3])
c = np.array([[1, 2],[3, 4]])


arr  = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + np.ones((1, 3)))
