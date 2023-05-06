# LC
# find vehicle name weight below 3000
dic={"Sedan":1500,"Suv":2000,"Pickup":2500,"Minivan":1600,"Van":2400,"Semi":13600,"Bicycle":7}
# print(dic)

# for i in dic:
#     print(i)

lst=[i.upper() for i in dic if dic[i]<3000]
print(lst)
