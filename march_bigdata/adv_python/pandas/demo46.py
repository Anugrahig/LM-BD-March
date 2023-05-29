# Fill missing value into specific column
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
df["Calories"].fillna(300,inplace=True)
print(df)
df["Date"].fillna("2020/12/02",inplace=True)
print(df)
