# join operation on data set
# custm.txt :cid,name,age,loc,salery
# order.txt: oid,pur_date,cid,p_amnt


# 1. id name,age,sal,dat,amt
# 2. salabove 2000 name,age,amnt,date,sal
# 3. age above 23 name,dat,amount
# 4. age max one emp name,age ,amount,date,sal
# 5. Latest date one employee name,age ,sal,date
import pandas as pd
import numpy as np
df1=pd.read_csv("Files/custom.txt",names=["cid","name","age","loc","sal"])
df2=pd.read_csv("Files/order.txt",names=["oid","pdate","cid","pamt"])
print(df1.head())
print(df2.head())
# df=pd.merge(df1,df2,on="cid")
# print(df.head())
print("*1*")
df3=pd.merge(df1,df2,on="cid")[["name","sal","pdate","pamt"]]
print(df3.head())
print("*2*")
# df3=df.loc[df["sal"]>2000][["name","age","pdate","pamt"]]
df3=pd.merge(df1,df2,on="cid").loc[df1["sal"]>2000][["name","age","pdate","pamt"]]
print(df3.head())
print("*3*")
df3=pd.merge(df1,df2,on="cid").loc[df1["age"]>23][["name","age","pdate","pamt"]]
print(df3.head())
print("*4*")
df3=pd.merge(df1,df2,on="cid").sort_values(by="age",ascending=False)[["name","age","pamt","pdate","sal"]].head(1)
print(df3)
print("*5*")
df3=pd.merge(df1,df2,on="cid").sort_values(by="pdate",ascending=False)[["name","age","pdate","sal"]].head(1)
print(df3)
# print(df)