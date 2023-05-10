# Reshape : used for changing order of an array : total number of elements should be same
# Flatten : convert all array into 1 Dimension
# Flatten used to reshape a matrix to 1 Dimensional
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.flatten()
print(b)