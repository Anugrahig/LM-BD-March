# even_numbers , odd_numbers list

f = open("sample2","r")
new_lst=[]
o_lst=[]
e_lst=[]

for i in f:
    new_lst.append(int(i.rstrip("\n")))

print(new_lst)


for i in new_lst:
    if i%2==0:
        e_lst.append(i)
    else:
        o_lst.append(i)
print("Even sum",sum(e_lst))
print("Odd sum",sum(o_lst))

