# Nested if
# second-largest number among 3 numbers Program
# num1,num2,num3

num1= int(input("Enter 1st Number : "))
num2= int(input("Enter 2nd Number : "))
num3= int(input("Enter 3rd Number : "))

if num1>num2 and num1>num3:
    if num2>num3:
        print("Second Largest Number is num2 ",num2)
    else:
        print("Second Largest Number is num3 ",num3)
elif num2>num3 and num2>num1:
    if num1>num3:
        print("Second Largest Number is num1 ",num1)
    else:
        print("Second Largest Number is num3 ",num3)
else:
    if num1>num2:
        print("Second Largest Number is num1 ",num1)
    else:
        print("Second Largest Number is num2 ",num2)





