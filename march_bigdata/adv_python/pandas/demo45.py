# Handling missing values : Dropna : dropna will delete all NaN rows
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df.head(10))
print(df.info())
# total num of missing value
print(df.isna().sum())
print()
print(df.shape)
# drop missing rows

df1=df.dropna()
print(df1.isna().sum())
print(df1.shape)
# It delete NaN values in the original data set
df.dropna(inplace=True,ignore_index=True)
df.fillna(300,inplace=True)
print(df)