import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])

# Row selections
print(array[0])        # First row
print(array[-1])       # Last row
print(array[0:2])      # First two rows
print(array[0:3:2])    # Rows 0 and 2
print(array[::2])      # Every second row
print(array[::-1])     # Reversed rows
print(array[::-3])     # Reversed every 3rd row

# Column selections
print(array[:, 0])         # First column
print(array[:, -2])        # Second-last column
print(array[:, 0:2])       # First two columns
print(array[:, ::2])       # Every second column
print(array[:, 1::2])      # Start from 1st col, skip every 2nd
print(array[:, ::-1])      # Reverse columns
print(array[:, ::-2])      # Reverse every 2nd column

# Combined slicing (rows and columns)
print(array[0:3, 0:2])     # Rows 0–2, Columns 0–1
print(array[0:2, 1:3])     # Rows 0–1, Columns 1–2
print(array[2:4, 0:2])     # Rows 2–3, Columns 0–1
print(array[2:4, 1:4])     # Rows 2–3, Columns 1–3
