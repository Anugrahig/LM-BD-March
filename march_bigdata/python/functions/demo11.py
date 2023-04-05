# Syntax

# import packagename.modulename
# variablename = packagename.modulename.functioncall()

# import functions.operation
# res= functions.operation.add(40,60)
# res1= functions.operation.sub(40,60)
# res2= functions.operation.div(40,60)
# res3= functions.operation.mul(40,60)
# print(res)
# print(res1)
# print(res2)
# print(res3)
# we have drawback in this method
# - import all modules functions
# to overcome this

from functions.operation import *
data = add(12,8)
print(data)
data1 = sub(12,8)
print(data1)
data2 = mul(12,8)
print(data2)
data3=div(12,8)
print(data3)


