# factorial of a given number

num = int(input("Enter the Limit : "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of number is",fact)
