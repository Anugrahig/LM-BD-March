# convert dictionary into series
# key will act as index in dictionary
import pandas as pd
import numpy as np
a=pd.Series({"one":1,"two":2,"three":3,"four":4,"five":5})
print(a)