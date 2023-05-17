import pandas as pd
import numpy as np
dic={"one":1,"two":2,"three":3,"four":4,"five":5}
# we can change the order using index property
a=pd.Series(dic,index=["five","four","three","two","one"])
print(a)