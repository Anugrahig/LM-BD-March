# Reshape : To change order of the matrix
# Resizing matrix should be same size (total no. of elements)
import numpy as np
a=np.array([[1,2,3,4,5],[5,6,7,8,5],[9,10,11,12,5],[13,14,15,16,5]])
print(a)
b=a.reshape([5,4])
# b=a.reshape([1,2,2])
print(b)
print(b.shape)

