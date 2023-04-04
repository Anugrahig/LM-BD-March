# lower limit
# upper limit

# lower to upper prime number


lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))

for i in range(lower,upper+1):
    for j in range(2,(i//2)+1):
        if i%j==0:
            break
    else:
        print(i)
