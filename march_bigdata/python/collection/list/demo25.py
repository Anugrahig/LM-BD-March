# binary search algorithm:
search = int(input("Enter number to Search : "))
lst=[2,3,1,7,15,10,13,9,4,5]

lst.sort()
print(lst)
low=0
upp=len(lst)-1
flag=0
# print(mid)
while low<=upp:
    mid=(low+upp)//2
    if search> lst[mid]:
        # print("Print2",flag)
        low=mid+1
    elif search< lst[mid]:
        upp=mid-1
    elif search==lst[mid]:
        flag=1
        break

if flag==1:
    print("Element Present")
else:
    print("Element not Present")

# 1.sort the list
# low=0
# upp= len(lst-1)
#
# calc mid=low+upp//2

#if search elem > lst[mid]
# low = mid+1

# if saerch <lst[mid]
# upp=mid-1

# if search == lst[mid]