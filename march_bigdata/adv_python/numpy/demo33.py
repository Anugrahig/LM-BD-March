# Sort in 1D
import numpy as np
a=np.array([1,6,8,2,10,16,1,5])
print(a)
# ascending order sort by default
b=np.sort(a)
print(b)
b=np.sort(a)
b=b[::-1]
print(b)
# 2nd method
a=np.array([1,6,8,2,10,16,1,5])
b=np.sort(a)[::-1]
print(b)
