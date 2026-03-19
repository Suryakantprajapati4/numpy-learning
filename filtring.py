"""
NumPy Filtering Example

This script demonstrates how to filter arrays using conditions in NumPy.
"""

import numpy as np

# Sample data
ages = np.array([
    [12, 34, 56, 78, 90, 53, 82],
    [40, 62, 91, 36, 73, 49, 79]
])

# Teenagers (age < 18)
teenagers = ages[ages < 18]
print("Teenagers:", teenagers)

# Adults (18 to 59)
adults = ages[(ages >= 18) & (ages < 60)]
print("Adults:", adults)

#Not Adults
#adults = ages[(ages<18) | (ages>=60)]


# Seniors (age > 65)
seniors = ages[ages > 65]
print("Seniors:", seniors)

# Even and Odd numbers
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print("Even numbers:", evens)
print("Odd numbers:", odds)

# Using np.where (replace values < 18 with 0)
filtered = np.where(ages >= 18, ages, 0)
print("Filtered (>=18):", filtered)
