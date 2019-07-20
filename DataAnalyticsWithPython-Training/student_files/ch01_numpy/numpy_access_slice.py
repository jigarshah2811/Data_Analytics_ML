import numpy as np

# Create NumPy Array
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])
print(arr)

# Accessing it
print("Accessing item, Axis0:1, Axis1:0")
print(arr[1, 0])
print("Accessing items range, Axis0: 1 onwards, Axis1: 1 onwards")
print(arr[1:, 1:])
print("Accessing items range, Axis0: 1 onwards till 3, Axis1: 2 onwards till 3")
print(arr[1:3, 1:3])
print("Accessing items range, Axis0: 0 onwards till 3 step 1, Axis1: 0 onwards till 3 step 1")
print(arr[0:3:2, 0:3:2])

# Modifying it
print("Modifying array")
arr[:,1] = 10
print(arr)
arr[:, [0,3]] = 10
print(arr)
arr[[0,3],:] = 20
print(arr)

# Selecting using boolean: Masking OR boolean enforcing
arr_bool = arr[:, np.array([True, False, True, False])]
print(arr_bool)

# Math operations, add +, substract -, Multiply *  (Use Operator instead of method, same)

# Transpose
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])
print("Original Array:\n", arr)
print("Transpose Array:\n", arr.transpose())

