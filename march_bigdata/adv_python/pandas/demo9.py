# DataFrame
# describe : numerical value mean,std
import pandas as pd
import numpy as np
data=[[101,"anu","ig",22,"Developer","TCR",10000],
   [102,"manu","nair",23,"Designer","TVM",15000],
   [103,"vinu","np",26,"Designer","CLT",13000],
   [104,"nandhu","np",27,"Designer","EKM",12500],
   [105,"aadarsh","nk",27,"Designer","PLK",16000],
   ]
# add column name to data
df=pd.DataFrame(data,columns=["id","fname","lname","age","prof","loc","sal"])
print(df)
print("***"*50)
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
# print(b[1:2][0:])

# describe:
# variance: difference from mean
# SD: is square root of variance

print(df.describe())
print()
# to describe string value : O : means object
print(df.describe(include="O"))
"""
       fname lname      prof  loc
count      5     5         5    5
unique     5     4         2    5
top      anu    np  Designer  TCR
freq       1     2         4    1
"""
# top: most repeated value : if unique it took first value
# freq: it's fequency of top

# describe all
print()
# to include all values : use all
print(df.describe(include="all"))
print()

# How to add new column
df["Dept"]=["ABC","DEF","HIG","LMN","OPQ"]
print(df)

print()
# To print columns
print(df[["fname","lname","age","prof"]])
print()
# to store values into another dataframe
df1=df[["fname","lname","age"]]
print(df1)
