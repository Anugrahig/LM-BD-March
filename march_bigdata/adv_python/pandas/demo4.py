import pandas as pd
import numpy as np
a=pd.Series([1,2,3,4,5])
b=pd.Series([6,7,8,9,10])

print(a)
print(b)

# append
# ignore_index = True means continuous index
c=a._append(b,ignore_index=True)
print(c)
