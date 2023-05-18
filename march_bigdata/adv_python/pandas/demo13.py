# read movies_cleaned_pandas file
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/movies_cleaned_pandas.csv")
df.columns=["id","name","year","rating","duration"]
# print(df.to_string())
# pd.set_option('display.max_columns', None)
print(df.to_csv())