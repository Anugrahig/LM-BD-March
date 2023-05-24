import pandas as pd
import numpy as np
df=pd.read_csv("Files/movies_cleaned_pandas.csv",names=["id","name","year","rating","dur"])
print(df.head())
# 1
print(df.count())
# 2
print(df.shape)
print(df.drop_duplicates())
print(df.shape)
# 3
df1=df.sort_values("year",ascending=False)["year"]
print(df1)
# 4
df1=df.sort_values("rating",ascending=False)[["name","year","rating"]].head(5)
print(df1.head(5))
# 5
df1=df.sort_values("rating")[["name","year","rating"]].head(3)
print(df1)
# 6
df1=df.groupby("year")["year"].count().sort_values(ascending=False)
print(df1.head(10))
# 7
df1=df.groupby("rating")["rating"].count().sort_values(ascending=False)
print(df1.head(10))

# 8
df1=df.loc[(df["year"]==2008) & (df["rating"]>3)]
print(df1.head(10))
# # a
print(df1.count())
# 9
df1=df.sort_values("dur",ascending=False)[["name","year","rating","dur"]].head(1)
print(df1)
# 10
df1=df.sort_values("rating")[["name","year","rating","dur"]].head(1)
print(df1)
# 11

df1=df.loc[(df["year"]>=2005) & (df["rating"]>=4)]
# print(df1.head(10))
#A
df2=df1.sort_values("rating",ascending=False).head(1)
print(df2.head())
#B
df2=df1.sort_values("rating").head(1)
print(df2)
print()
# 12

print(df)

df1=df.loc[df["year"]==2005].count()
print(df1)

# 13
df1=df.loc[(df["year"]>=1975)&(df["year"]<=2008)].count()
print(df1)
# 14
df1=df.loc[(df["year"]>=1975)&(df["year"]<=2008)&(df["rating"]>3.5)].count()
print(df1)
