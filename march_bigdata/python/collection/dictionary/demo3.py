pattern="ABCDBCDFGHCDSD"
dic={}

for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i)
        break

# print(dic[0])

