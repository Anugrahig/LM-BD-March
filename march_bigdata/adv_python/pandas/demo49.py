# how to handle wrong formatted data
# wrong formatted data : if data is huge value (not possible) that value occur
# eg: height : 500cm weight: 500kg
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
# 7        450  '2020/12/08'    104       120     253.3
df.loc[7,"Duration"]=45
print(df)
df.dropna(inplace=True)
df.loc[7,"Duration"]=df["Duration"].mode()[0]
# df["Duration"].fillna(df["Duration"].mode()[0],inplace=True)
print(df)
print()

