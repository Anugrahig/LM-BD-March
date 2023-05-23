import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
print(df.head(5))
print("**"*50)

df1=df.groupby(["prof"])["prof"].count().sort_values(ascending=False)
print(df1)
print("**"*5)
# prof count &
df1=df.sort_values(by="prof",ascending=False)
# df1=df.groupby(["prof"]).count().sort_values(by="prof")
print(df1)
print("**"*50)
# loc count

df1=df.groupby(["loc"])["loc"].count().sort_values(ascending=False)
print(df1)
# get row count
print(df.count())
print(df.head())


