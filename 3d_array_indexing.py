# 3d_array_indexing.py
# Example: Working with 3D NumPy arrays
# Demonstrates ndim, shape, indexing, and custom string creation

import numpy as np

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','','']]])

print("Dimensions:", array.ndim)      # Output: 3
print("Shape:", array.shape)          # Output: (3, 3, 3)

print("Value at [2][1][0]:", array[2][1][0])      # Output: V
print("Value at [1,0,2]:", array[1,0,2])          # Output: L

# Combining values to form a word
word = array[2,0,0] + array[2,0,2] + array[1,2,2] + array[2,2,0]
print("Formed Word:", word)          # Output: SYRY
