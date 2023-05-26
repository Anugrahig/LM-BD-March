# right outer join
import pandas as pd
import numpy as np
df1=pd.DataFrame(
    {"id":[1,2,3,4,5,6],
    "fname":["anu","vinu","manu","rinu","binu","sinu"],
     "lname":["nair","menon","lk","lp","sn","rk"],
     "age":[21,22,23,24,25,26]
     }
)
print(df1)
print()
df2=pd.DataFrame(
    {"id":[4,5,6,7,8,9],
    "prof":["Developer","Designer","Teacher","HR","Designer","Manager"],
     "sal":[12000,16000,15000,14000,13000,17000],
     "loc":["TCR","TVM","CLT","PLK","EKM","KNR"]
     }
)
print(df2)
df=pd.merge(df1,df2,on="id",how="right")
print(df)