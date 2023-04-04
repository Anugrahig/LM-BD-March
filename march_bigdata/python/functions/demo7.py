# factorial of a number 3 function methods
# Method1
def fact():
    num = int(input("Enter a number : "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Result = ", fact)


fact()

print()


# Method2
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Result = ", fact)


fact(int(input("Enter a number : ")))

print()


# Method3
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


print(fact(int(input("Enter a number: "))))
