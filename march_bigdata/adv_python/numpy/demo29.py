# Dot product
import numpy as np
a=np.arange(1,4)
b=np.arange(3,0,-1)

print(a)
print(b)

# Dot product
# [1*3+2*2+3*1]
c=np.dot(a,b)
print(c)

a=np.array([[3,4,5],[5,4,3],[4,3,2]])
b=np.array([[3,2,1],[5,4,3],[9,4,3]])
# [3*3+4*5+5*9 3*2+4*4+5*4 3*1+4*3+5*3]
# [5*3+4*5+3*9 5*2+4*4+3*4 5*1+4*3+3*3]
# [4*3+3*5+5*9 4*2+3*3+2*4 4*1+3*3+2*3]
