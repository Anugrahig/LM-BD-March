# filtering : using loc
import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","pro","loc"])
print(df.head())
df1=df.loc[df["age"]>55]
print()
print(df1.head())

df2=df[df["age"]==25]
print(df2)
print()
print()
df3=df[df["loc"]=="india"]
# df3=df.iloc[df["loc"]=="india"]
print(df3)

