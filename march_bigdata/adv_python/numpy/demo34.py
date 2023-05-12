# Sorting 2D row & column wise
import numpy as np
a=np.array([[6,19,7,10],[5,1,10,6],[2,9,10,1],[1,10,11,15]])
print(a)
print()
# by default 2D array is row wise sort (ascending order)
# similar to sort(a,axis=1(row))
b=np.sort(a)
print(b)
print()
# column wise sort
b=np.sort(a,axis=0)
print(b)
# sort to 1D
c=np.sort(a,axis=None)
print(c)

