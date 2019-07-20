"""
        task1_1.py solution -
                                (Part 1) -       create a checkerboard pattern
                                (Part 2) -       n x n for advanced solution
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------
# Part 1 - Creates an 8x8 checkerboard array.
#
print('An 8x8 board...')
row = np.array([0, 1]*4)                                         # create alternating 1D array with a length of 8
row_shifted = np.roll(row, 1)                                   # create another array opposite of the first
partial_checkerboard = np.column_stack((row, row_shifted))      # combine them
checkerboard = np.tile(partial_checkerboard, [1, 4])            # repeat the combined array 4 more times
print(checkerboard)


# -----------------------------------------------------------------
# Part 2 - Alternate version, this version creates an n x n checkerboard
#
print('An n x n board...')
width = 5
try:
    width = int(input('Enter width of board: '))                          # length of the board
except ValueError:
    print('Invalid size value--using {0}.'.format(width))

row = np.zeros(width, dtype=int)                                # 0 0 0 0 0
row[1::2] = 1                                                   # 0 1 0 1 0
row_inverted = np.logical_not(row)                              # 1 0 1 0 1
two_rows = np.stack([row, row_inverted], axis=0)                # give two alternating rows stacked
larger_board = np.tile(two_rows, [int(np.ceil(width/2)), 1])    # repeats vertically, odds will be larger than necessary
checkerboard = larger_board[:width]                             # select only a board of size width x width
print(checkerboard)

