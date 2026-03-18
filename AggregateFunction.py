#aggregate Fuction = summarize data and typically return a single value

import numpy as np
array= np.array([[1,2,3,4],
                 [5,6,7,8]])

#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array))
#print(np.var(array))
#print(np.min(array))
#print(np.max(array))
#print(np.argmin(array))
#print(np.argmax(array))


# Sum of entire array
print("Total Sum:", np.sum(array))

# Sum column wise
print("Column Sum:", np.sum(array, axis=0))

# Sum row wise
print("Row Sum:", np.sum(array, axis=1))
