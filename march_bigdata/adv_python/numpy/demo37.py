# argsort: sorted index value will be return
import numpy as np
a=np.array([6,0,3,9,15,4,2,11,12])
c=np.sort(a)
print(c)
# [1,6,2,5,0,3,7,8,4]
b=np.argsort(a)
print(b)

# 6 : 0       4 : 5
# 0 : 1      2 : 6
# 3 : 2      11 : 7
# 9 : 3      12 : 8
# 15 : 4