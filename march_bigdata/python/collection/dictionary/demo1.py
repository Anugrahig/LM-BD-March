# Dictionary

dic={
    "id":101,"fname":"vinay","lanme":"k","age":25,"prof":"bigdata"
}
# print(dic)

# particular values
# corresponding key

print(dic["age"])
print(dic["fname"])

print()

# print these details
# id,101
# fname,"vinay"
# lanme, "k"
# age , 25
# prof : bigdata

for i in dic:
    print(i,",",dic[i])
print()
# age:25 ==> 30

dic["age"]=30
print(dic)

print()

# insert a new value
dic["salary"]=1000
# update salary vale
dic["salary"]+=500
print(dic)

print()
# delete key value pair

del dic["prof"]
print(dic)

print()
# in operation dictionary
print("id" in dic)
print()
# in operation dictionary
print("age" not in dic)
