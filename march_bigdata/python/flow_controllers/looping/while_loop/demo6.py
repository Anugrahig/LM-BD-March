# sum of n numbers
# read
# eg lim =10
# 1+2+3+...10=55

lim = int(input("Enter the limit : "))
i = 1
total = 0
while i <= lim:
    total = total+i
    i += 1
print("Sum = ",total)

