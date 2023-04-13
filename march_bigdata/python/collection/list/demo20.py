#  remove duplicate elements in a lst
n_lst=[]
lst=[10,10,20,30,40,50,60,70,50,40,30,100,50,40,30,10,25,40]
for i in lst:
    if i not in n_lst:
        n_lst.append(i)
print(n_lst)