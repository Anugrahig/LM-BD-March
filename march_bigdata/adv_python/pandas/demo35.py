# Max: maximum will affect more than one field in a dataframe
# min
# Max
# Mean
# Sum
import pandas as pd
import numpy as np
df=pd.read_csv("Files/Temperature",sep=" ",names=["year","temp"])
print(df.head())
# df1=df.groupby("colname")["colname"].max()
# find year wise maximum temp
print()
df1=df.groupby("year")["temp"].max().sort_values(ascending=False)
print(df1)
# Min:
print()
df1=df.groupby("year")["temp"].min().sort_values(ascending=False)
print(df1)
# Sum()
print()
df1=df.groupby("year")["temp"].sum().sort_values(ascending=False)
print(df1)

# Avg
print()
df1=df.groupby("year")["temp"].mean().sort_values(ascending=False)
print(df1)

