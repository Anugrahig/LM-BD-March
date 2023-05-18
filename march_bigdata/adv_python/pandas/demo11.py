# External data set into Dataframe
import pandas as pd
import numpy as np
# if the data is space separated file then use sep=","
# if the doesn't contain header then we need to specify header None
df=pd.read_csv("./Files/customer.csv",header=None)
df.columns=["id","fname","lname","age","prof","loc"]
df1=df[["fname","lname","age","prof"]]
print(df1)

