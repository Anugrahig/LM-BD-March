# convert dictionary into dataframe
import pandas as pd
import numpy as np
dic={
    # "id":[101,102,103,104,105],

      "name":["anu","manu","vinu","binu","rinu"],
      "age":[22,23,24,25,26],
      "address":["PLK","CLT","TVM","TCR","EKM"],
      "qualification":["MCA","MBA","BCA","B.com","M.com"]
      }
df=pd.DataFrame(dic)
print(df)
print(df.shape)
print(df.size)
# to print column names of dataframe
print(df.columns)
# In pandas object is datatype instead of string
print(df.dtypes)

print(df.describe())
print()
df["salery"]=[12000,13000,14000,15000,16000]
print(df)