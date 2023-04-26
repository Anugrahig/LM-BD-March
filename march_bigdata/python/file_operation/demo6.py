# age above 25
f=open("customer","r")
prof_dic={}
for i in f:
    data=i.rstrip("\n").split(" ")
    if data[3] > "25":
        print(data[1:5])
        if data[4] in prof_dic:
            prof_dic[data[4]]+=1
        else:
            prof_dic[data[4]]=1
print(prof_dic)

"""
print(i[1:5])
id:0
fname:1
lname:2
age:3
prof:4
loc:5
"""
