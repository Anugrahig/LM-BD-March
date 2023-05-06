# lst=[1,4,6,7,5,3,2,4,6,8,9,12,13,11,10,7,6,5,3,7,8]
# o/p:
# [1,7,2,13,3]
# lst=[1,4,6,7,5,3,2,4,6,8,9,12,13,11,10,7,6,5,3,7,8]
lst=[1,3,5,6,8,9,6,4,3,2,5,8,9]
print(lst)

len_s=len(lst)
print()
res=[]
for i in range(len(lst)):
    if i==0:
        res.append(lst[i])
    j=i+1
    k=i+2
    if len_s>j and len_s>k:
        if lst[i]<lst[j]>lst[k]:
            res.append(lst[j])
        elif lst[i]>lst[j]<lst[k]:
            res.append(lst[j])
    else:
        break
print(res)
# second logic

for i in range(0,len(lst)-1):
    if ((lst[i-1]<lst[i]>lst[i+1]) or (lst[i-1]>lst[i]<lst[i+1])):
        print(lst[i])






# lst=[1,2,9,7,6,4,3,6,8,9,11,12,10,7,6,5,4,3,8,9,10,11,9,7,6]




















