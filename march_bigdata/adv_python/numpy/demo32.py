# Sum of 2D array
import numpy as np
a=np.arange(1,17).reshape(4,4)
print(a)
b=np.sum(a)
print(b)
# axis : used find row wise sum and column wise sum
# axis=0 means columns wise ,axis=1 means row wise sum

print()
b=np.sum(a,axis=0)
print(b)
# [1+5+9+13]
# [2+6+10+14]
# [3+7+11+15]
# [4+8+12+16]

# row wise column
print()
b=np.sum(a,axis=1)
print(b)
# [1+2+3+4]
# [5+6+7+8]
# [9+10+11+12]
# [13+14+15+16]
