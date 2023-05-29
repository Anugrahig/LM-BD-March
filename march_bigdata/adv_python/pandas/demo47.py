# Fill missing value into specific column basis (mean,median,mode:most repeated value)
# Object data filled with mode value

import pandas as pd
import numpy as np
df=pd.read_csv("Files/missing_data1.csv")
print(df)
# fill NaN value with mean value
# df["Calories"].fillna(df["Calories"].mean(),inplace=True)
print(df)
# fill NaN value with median value
# df["Calories"].fillna(df["Calories"].median(),inplace=True)
df["Calories"].fillna(df["Calories"].mode()[0],inplace=True)
print(df)


