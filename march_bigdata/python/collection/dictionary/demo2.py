# word count problem

# cat rat bat cat rat bat car car car bat bat car bus car bus rat

# cat,2
# rat,3
# bat,4
# car,5
# bus,2
dic={}
data = "cat rat bat cat rat bat car car car bat bat car bus car bus rat"
data1=data.split(" ")
print(data1)
for i in data1:
    # print(i)
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)