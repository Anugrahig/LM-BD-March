# lower upper
# sum of odd numbers
lower = int(input("Enter the Lower limit : "))
upper = int(input("Enter the Upper limit : "))
odd_sum=0
while lower <= upper:
    if lower%2 == 1:
        odd_sum=odd_sum+lower
    lower += 1
print("Sum = ",odd_sum)

