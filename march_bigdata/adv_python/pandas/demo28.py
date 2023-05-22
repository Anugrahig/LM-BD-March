# 1 age descending order fname,lname,age,country
# 2 loc=="india" fname,age,prof : fname - acsend
# 3  loc="us" full data
# 4  loc ="india , age above 40 , fname,lname,age prof,loc
# 5  loc ="us" , age max 5 employee , fname,lname,age
# 6  loc ="india , age min 3 , employee fname,lname,age,loc
# 7  age range 40 to 60, fname,lname,age prof
# 8  loc="us  age range b/w 25 - 35, fname,lname,age
# 9  prof="Pilot full data
# 10 prof="Pilot" and age max,  employee fname,lname,age

import pandas as pd
import numpy as np
df=pd.read_csv("Files/customer.csv",names=["id","fname","lname","age","prof","loc"])
print(df.head())
print("*"*150)
df1=df.sort_values(by="age",ascending=False)[["fname","lname","age","loc"]]
print(df1.head())
print("*"*150)
df1=df.sort_values(by="fname").loc[df["loc"]=="india"][["fname","age","prof"]]
print(df1.head())
print("*"*150)
df1=df.loc[df["loc"]=="us"]
print(df1.head())
print("*"*150)
df1=df.loc[(df["age"]>40)&(df["loc"]=="india")][["fname","lname","age","prof","loc"]]
print(df1)
print("*"*150)
df1=df.sort_values(by="age").loc[df["loc"]=="us"][["fname","lname","age"]].head(5)
print(df1)
print("*"*150)
df1=df.sort_values(by="age",ascending=True)[["fname","lname","age","loc"]].head(3)
print(df1)
print("*"*150)
df1=df.loc[(df["age"]>40) & (df["age"]<60)][["fname","lname","age","prof"]]
print(df1.head(5))
print("*"*150)
# df1=df.loc[(df["age"]>40) & (df["age"]<60) ].loc[df["loc"]=="us"][["fname","lname","age"]]
df1=df.loc[(df['loc'] == 'us') & (df['age'] >= 25) & (df['age'] <= 35)][["fname","lname","age"]]
print(df1.head())
print("*"*150)
df1=df.loc[df["prof"]=="Pilot"].head()
print(df1)
print("*"*150)
df1=df.sort_values(by="age",ascending=False).loc[df["prof"]=="Pilot"][["fname","lname","age"]].head(1)
print(df1)

