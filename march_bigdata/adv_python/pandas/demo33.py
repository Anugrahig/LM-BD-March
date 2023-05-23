# customer assignment
import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
# 1
print(df.count())
print()
# 2
print(df.shape)
print()
df1=df.drop_duplicates()
print(df1.shape)
print()
# 3
df1=df.sort_values(by="age",ascending=False)[["fname","lname","prof","loc"]].head(10)
print(df1)
print()
# 4
df1=df.sort_values(by="age")[["fname","lname","prof","loc"]].head(5)
print(df1)
print()
# 5
df1=df.groupby(by="loc")["loc"].count().sort_values(ascending=False)
print(df1)
print()
# 6
df1=df.loc[df["loc"]=="australia"]
print(df1)
print()
# 7
df1=df.groupby(by="age")["age"].count().sort_index(ascending=False)
print(df1)
# 8
df1=df.groupby(by="prof")["prof"].count().sort_values(ascending=False)
print(df1)
# 9
df1=df.loc[df["loc"]=="india"]
print(df1.head(4))
# a
print(df1.count())
# b
df2=df1.groupby(by="prof")["prof"].count().sort_values(ascending=False)
print(df2)
# c
df2=df1.sort_values(by="age",ascending=False)[["fname","lname","age","prof"]].head(3)
print(df2)
# d
df2=df1.sort_values(by="age")[["fname","lname","age","prof"]].head(3)
print(df2)
# e
df2=df1.loc[df["age"]>40]
print(df2)
# f
df2=df1.loc[(df1.age>=30)&(df1.age<=40) ].groupby(by="prof")["prof"].count()
print(df2)
print()
# 10
df1=df.loc[df["loc"]=="us"]
print(df1.head(5))
# a
print(df1.count())
# b
df2=df1.groupby(by="age")["age"].count()
print(df2)
# c
df2=df1.groupby(by="prof")["prof"].count().sort_values(ascending=False)
print(df2)
# d
df2=df1.loc[(df1["prof"]=="Civil engineer")&(df1["age"]>30)]
print(df2)