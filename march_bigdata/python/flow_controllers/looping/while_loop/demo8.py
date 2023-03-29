# Factorial of a given number

num= int(input("Enter the number = "))
i=1
fact=1
while i <= num:
    fact = i*fact
    i += 1
print("Factorial of ",num,"is : ",fact)

