# Fill missing value into specific column
import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
# df["Date"].dropna(inplace=True)
df.dropna(subset=["Date"],inplace=True,ignore_index=True)
print(df)
df.dropna(subset=["Calories"],inplace=True,ignore_index=True)
print(df)