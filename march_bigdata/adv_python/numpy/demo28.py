# Mathematical array poeration
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[9,8,7],[6,5,4],[3,2,1]])

# 1.Addition
# Order should be same
c=np.add(a,b)
print(c)
print(a+b)

# 2.Subtraction
c=np.subtract(a,b)
print(c)

# 3.Multiplication : element by element : (not dot product)

print("----")
c=np.multiply(a,b)
print(c)

# 4. Divison : Element by element
c=np.divide(a,b)
print(c)

# find square of elements
c=np.square(a)
print(c)

# Square root
c=np.sqrt(c)
print(c)




