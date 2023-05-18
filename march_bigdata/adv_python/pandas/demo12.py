# read sample4.txt file
import pandas as pd
import numpy as np
df=pd.read_csv("./Files/sample4.txt")
# print(df)
df.columns=["id","fname","lname","age","phon","loc"]
print(df)