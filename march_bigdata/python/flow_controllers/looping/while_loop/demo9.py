# read lower to upper print even in the range
lower = int(input("Enter the Lower Limit : "))
upper = int(input("Enter the Upper Limit : "))
print("Even Numbers are : ")
while lower <= upper:
    if lower % 2 == 0:
        print(lower)
    lower += 1


