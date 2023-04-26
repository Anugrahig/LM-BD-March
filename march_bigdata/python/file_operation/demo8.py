
# age above 40 fname,lname,age,prof
# india work,fname,lname,age,prof
# age above 50 and work lock uk print 1 to 5
# each prof count
# each loc count

f=open("C:/Users\Asus\Downloads\customer.csv","r")
# for i in f:
#     data=i.strip("\n").split(",")
#     print(data)
#     if data[3]>"40":
#         print(data[1:5])
# print()
# for i in f:
#     data = i.strip("\n").split(",")
#
#     if data[-1]=="india":
#         print(data[1:6])
# print()
# for i in f:
#     data = i.strip("\n").split(",")
#
#     if data[3]>"50" and data[5]=="uk":
#         print(data[1:5])
# print()
# prof count
# prof_count={}
#
# for i in f:
#     data = i.strip("\n").split(",")
#
#     if data[4] in prof_count:
#         prof_count[data[4]] += 1
#     else:
#         prof_count[data[4]] = 1
# for k,v in prof_count.items():
#     print(f"{k} , {v}")
# print(prof_count)

loc_count={}
for i in f:
    data=i.rstrip("\n").split(",")
    if data[-1] not in loc_count:
        loc_count[data[-1]]=1
    else:
        loc_count[data[-1]] += 1
# print(loc_count)

for k,v in loc_count.items():
    print(f"{k},{v}")
"""

0:id
1:fname
2:lname
3:age
4:prof
5:loc
"""