# Series
# -------
import pandas as pd
import numpy as np
a=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a)
print(type(a))
print(a.shape)
# head: first 5 element or 5 rows
print(a.head())

# tail : last 5 elements or 5 row
print(a.tail(4)) # last 4
