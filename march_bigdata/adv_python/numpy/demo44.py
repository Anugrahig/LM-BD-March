# search in 2D array
import numpy as np
a=np.array([[1,2,3],[3,2,1],[4,3,5]])
print(a)
b=np.where(a==5)
print(b)
# (array([2]), array([2]))
# 2nd row 2nd column
print()
b=np.where(a==3)
print(b)