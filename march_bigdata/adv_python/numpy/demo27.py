# 2 Dimensional Slicing
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
print(a)
# print(a[row,column])
print(a[:2,:3])

print(a[:4,:3])

print(a[:3,1:4])

print(a[1:5,2:4])

print(a[2:,:])

print(a[:4:2,1:4:2])

print(a[::2,1::2])

# zeroth column of data
# zeroth row of data
print(a[0,:])
print(a[:,0])


