# isna sum method is used find na values count
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/missing_data1.csv")
print(df.head(5))
# x=df.iloc[:,:-1]
# print(x)
# y=df.iloc[:,-1]
# print()
# print(y)

print(df.isna().sum())
# used fill data with 23
print(df.fillna(23))