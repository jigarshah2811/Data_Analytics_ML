"""
        task1_1_starter.py -
                                (Part 1) -       create a checkerboard pattern
                                (Part 2) -       n x n for advanced solution

                                The hints provided below represent only 1 way to accomplish this task and you
                                may take your own approach if you wish.

"""
import numpy as np

# Part 1 - Create an 8x8 checkerboard array.
#
# Hints: Step 1) create an array of alternating values of 1's and 0's
#        Step 2) create an array of the "opposite" values
#        Step 3) stack the arrays
#        Step 4) repeat the stacked array 4 more times
#        Step 5) display the checkerboard


def createBoard(rows, cols):
    arr0 = np.zeros([rows, cols], dtype=np.int)
    print("Accessing alternative column value")
    print("Step 1) create an array of alternating values of 1's and 0's")
    arr0[0::2, 1::2] = 1
    arr0[1::2, 0::2] = 1
    print(arr0)

    print("Step 2) create an array of the opposite values")
    arr1 = np.flip(arr0)
    print(arr1)

    print("Step 3) stack the arrays")
    return np.stack([arr0, arr1])


createBoard(8, 8)

# Part 2 - Create an n x n checkerboard
#
# Hints: Step 1) Specify a width for the checkerboardand create a 1-D array, a row, with all zeroes the length of "width"
#        Step 2) Use slicing to create alternating 1's in every other position
#        Step 3) Use np.logical_not(arr) to create an alternate array with the 1's and 0's reversed (inverted)
#        Step 4) Stack the two rows
#        Step 5) Repeat the two rows vertically (note: it may end up larger than width if width is odd)
#        Step 6) Use slicing to only take "width" number of rows