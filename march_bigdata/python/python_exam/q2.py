# Fibonacii of a given number

upp=int(input("Enter the limit: "))
n1=0
n2=1
# fib=0
print("Fibonacci series : ")
print(n1)
print(n2)
for i in range(1,upp):
    fib=n1+n2
    n1=n2
    n2=fib
    if upp+1<=fib:
        break
    else:
        print(fib)



