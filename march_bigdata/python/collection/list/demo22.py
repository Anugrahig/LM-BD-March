# List slicing
# -------------

lst=[20,10,15,25,40,45,60,75,41,29,27,21,19,14,61]

print(lst[2:8])

# print(lst[5:10])

# print(lst[2:4])

print(lst[4:])
# print(lst[7:])

print(lst[:6])
# print(lst[:4])

# entire list
print(lst[:])

# update with step value
print(lst[2:9:2]) #2,4,6,8

print(lst[4:11:3]) # 4,7,10


print(lst[3::3]) # not last index 15 3,6,9,12

print(lst[:8:2])

print(lst[::5]) # 0,5,10 index


# postive indexing
# 0 to n-1

# negative indexing
# -1 to -n
# eg: -1 to -15
print(lst[-15])
