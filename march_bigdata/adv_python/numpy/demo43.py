# Search
import  numpy as np
a=np.array([4,9,1,4,5,3,2,0,4,8])
print(a)
b=np.where(a==4) #index value
print(b)
print("--- "*50)
b=np.where(a%2==0)
print(b) # index position of even numbers

