# Identity Matrix
# Matrix should be square matrix Diagonal elements will be 1 ,Other elements will be 0
"""
[1 0 0]
[0 1 0]
[0 0 1]

[1 0 0 0]
[0 1 0 0] Not a diagonal matrix
[0 0 1 0]

"""
import numpy as np
a=np.identity(3,dtype=int)
print(a)
# second method
a=np.eye(4,dtype=int)
print(a)
