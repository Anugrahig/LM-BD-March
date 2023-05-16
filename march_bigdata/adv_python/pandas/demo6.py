import pandas as pd
import numpy as np
a=pd.Series([2,3,4,5])
b=pd.Series([4,5,6,7])
c=a.__add__(b)
d=a.__sub__(b)
e=a.__mul__(b)
f=a.div(b)
print(c)
print(d)
print(e)
print(f)
# Nan:Not an Number