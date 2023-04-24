# wordcount in a file
f=open("sample3","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(" ")
# print(data)

    for j in data:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
print(dic)