# rename column names
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/Iris.csv")

df1=df.rename(columns={"SepalLengthCm":"seplen","PetalLengthCm":"petlen"})
print(df1.head())
