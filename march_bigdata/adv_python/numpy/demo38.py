#
import numpy as np
a=np.array([3,4,1,2,4,5,11,0,4,5])
print(a)
for i in a:
    print(i)

print("==="*60)
a=np.array([[6,19,7,10],[5,1,10,6],[2,9,10,1],[1,10,11,15]])
for i in a:
    for j in i:
        print(j)

# 3D array need 3 for loops