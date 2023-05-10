
# 4*4 conver to (8,2)
# 3D
# 1D
import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a)
b=a.reshape([8,2])
print(b)
c=a.reshape([1,2,8])
print(c)
d=a.reshape([16])
print(d)
