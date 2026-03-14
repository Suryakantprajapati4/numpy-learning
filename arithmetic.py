import numpy as np

# Scalar arithmetic 

array = np.array([1,2,3])

print(array+1)
print(array-1)
print(array*100)
print(array/5)
print(array**4)


# vectorized math function
array = np.array([1,2,4])

print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))

#exercise
radii = np.array([1,2,3])
print(np.pi * radii ** 2)


# element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)


# Comparison operators
scores = np.array([60,100,80,45,67,90])
print(scores == 100)
print(scores >= 60)


# if the score is less than 60, make it 0
scores[scores < 60] = 0

print("Updated Scores:", scores)