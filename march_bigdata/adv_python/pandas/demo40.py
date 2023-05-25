# merge
# std : name,roll_no
# result: roll_no,resul

# 1. pass name,roll,res

import pandas as pd
import numpy as np
df1=pd.read_csv("Files/student",names=["name","rollno"])
df2=pd.read_csv("Files/results",names=["rollno","result"])
print(df1.head())
print(df2.head())
print("****")
df3=pd.merge(df1,df2,on="rollno").loc[df2["result"]=="pass"]
print(df3)