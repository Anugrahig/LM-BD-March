# 2 D array joining
import numpy as np
a=np.array([[6,19,7],[5,1,10],[2,9,10]])
b=np.array([[4,12,6],[9,5,16],[5,1,16]])
print(a)
print(b)
print("==="*50)
c=np.concatenate([a,b],axis=0) # default is column based
print(c)
print("==="*50)
c=np.concatenate([a,b],axis=1) #  row based
print(c)



