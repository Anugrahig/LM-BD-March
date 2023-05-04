#  1to 30 range even print even odd print odd

lst=[(i,"odd") if i%2==1 else (i,"even") for i in range(1,31)]
# print(lst)

# 1 to 50 range less than 15 small , 15 t0 35 range medium ,35 above large

lst=[ "small" if i<=15 else "medium" if i<=35 else "large" for i in range(1,51)]
# print(lst)

# 1 to 75 range  1 to 10 a+ 11 to 30 A 31 to 50 B+ 51 to 75 B
lst=[(i,"A+") if i<=10 else (i,"A") if i<=30 else (i,"B+") if i<=50 else (i,"B") for i in range(1,76)]
print(lst)