# 15 t0 50 elements array then odd numbers arrays
import numpy as np
a=np.arange(15,51)
print(a)
b=a%2==1
print(a[b])