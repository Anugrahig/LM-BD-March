# 1. age above 23- fname,lname,age
# 2. age maximum 2 employee fname,lname,age,phone
# 3. age minimum 1 employee fname,lname,age,phone,loc
# 3. loc=="chennai,age max 1 employee fname,lname,ge,phone

# loc,sort,column,head/tail
import pandas as pd
import numpy as np
df=pd.read_csv("Files/sample4.txt",names=["id","fname","lname","age","num","loc"],index_col=0)
print(df.head())
# 1
print()
df1=df.loc[df["age"]>23] [["fname","lname","age"]]
print(df1)

print()


df2=df.sort_values(by="age",ascending=False)[["fname","lname","age","num","loc"]].head(2)
print(df2)
print()

df2=df.sort_values(by="age",ascending=False)[["fname","lname","age","num","loc"]].tail(1)
print(df2)
print()

df3=df.loc[df["loc"]=="chennai"].sort_values(by="age",ascending=False)[["fname","lname","age","num"]].head(1)
print(df3)
