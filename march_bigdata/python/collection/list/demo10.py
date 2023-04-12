# empty list 1 to 100 elements add
# even==> even_list
# odd==> odd_list

# lst sum
# even_lst==> total
# odd_lst==> total

lst=[]
e_lst=[]
o_lst=[]
for i in range(1,101):
    lst.append(i)
# print(lst)
for i in lst:
    if i%2==0:
        e_lst.append(i)
    else:
        o_lst.append(i)
print("Total :",sum(lst))
print("Sum of even numbers: ",sum(e_lst))
print("Sum of even numbers: ",sum(o_lst))
