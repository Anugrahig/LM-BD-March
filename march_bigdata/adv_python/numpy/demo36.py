#
import numpy as np
a=np.array([[6,19,7,10],[5,1,10,6],[2,9,10,1],[1,10,11,15]])
print(a)
# find maximum in the array
b=np.max(a)
print(b)
print()
# find column wise maximum
c=np.max(a,axis=0)
print(c)
# find row wise maximum
print()
c=np.max(a,axis=1)
print(c)

# Min
print()
c=np.min(a)
print(c)
print()
# find column wise min
c=np.min(a,axis=0)
print(c)

# find row wise max
print()
c=np.min(a,axis=1)
print(c)