# Nested List:
# list inside another list
lst=[
    [101,"vinay","k",26,"bigdata",1000],
    [102,"anu","p",27,"python",1500],
    [103,"amal","k",30,"bigdata",1750],
    [104,"arjun","p",29,"python",2000],
    [105,"varun","nair",24,"java",1800],
    [106,"hari","krishanan",36,"AI",3000],
    [107,"nithin","abraham",25,"web development",1500],
     ]
# for i in lst:
    # print(i)

# print fname,lname,age,prof

for i in lst:
    print(i[1:5])

print()

# print fname.age,salery

for i in lst:
    print(i[1:])

print()

# age above 28 print fname,lname,age,prof,sal

for i in lst:
    if i[3]>28:
        print(i[1:])

print()

# prof bigdata print fname,age,saalery

for i in lst:
    if i[4]=="bigdata":
        print(i[1::2])

print()

# age above 25 & salery above 1500
# print fname,lname,age,prof

for i in lst:
    if i[3]>24 and i[5]>1500:
        print(i[1:5])
print()

# calculate total salery
total=0
for i in lst:
    total=i[5]+total
print("Total = ",total)
