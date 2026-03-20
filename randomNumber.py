"""
NumPy Random Number Examples
---------------------------
This script demonstrates how to generate random numbers,
shuffle arrays, and select random elements using NumPy.
"""

import numpy as np

# ================================
# RANDOM INTEGER GENERATION (NEW METHOD)
# ================================

# Create a random number generator
rng = np.random.default_rng()

# Generate a single random integer between 1 and 10999
print("Single random integer:")
print(rng.integers(1, 10999))

# Generate 6 random integers between 1 and 1888
print("\nArray of 6 random integers:")
print(rng.integers(low=1, high=1888, size=6))

# Generate a 3x4 matrix of random integers between 1 and 100
print("\n3x4 matrix of random integers:")
print(rng.integers(low=1, high=101, size=(3, 4)))


# ================================
# RANDOM FLOAT GENERATION (OLD METHOD)
# ================================

# Set seed for reproducibility
np.random.seed(seed=1)

# Generate a single random float between 0 and 1
print("\nSingle random float:")
print(np.random.uniform())

# Generate 1 random float between -1 and 1
print("\nRandom float between -1 and 1:")
print(np.random.uniform(low=-1, high=1, size=1))

# Generate a 4x6 matrix of random floats between -1 and 1
print("\n4x6 matrix of random floats:")
print(np.random.uniform(low=-1, high=1, size=(4, 6)))


# ================================
# SHUFFLING AN ARRAY
# ================================

rng = np.random.default_rng()

array = np.array([1, 2, 3, 4, 7, 9])

# Shuffle the array in-place
rng.shuffle(array)

print("\nShuffled array:")
print(array)


# ================================
# RANDOM CHOICE FROM ARRAY
# ================================

fruits = np.array(["apple", "banana", "orange", "pineapple", "blackberry"])

# Select a single random fruit
fruit = rng.choice(fruits)
print("\nRandom fruit:")
print(fruit)

# Select 4 random fruits
selected_fruits = rng.choice(fruits, size=4)
print("\n4 random fruits:")
print(selected_fruits)

# Select a 3x4 matrix of random fruits
selected_fruits_matrix = rng.choice(fruits, size=(3, 4))
print("\n3x4 matrix of random fruits:")
print(selected_fruits_matrix)
