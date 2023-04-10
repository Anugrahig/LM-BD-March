# Prime number 1 to 100:
print("Prime Numbers are : ")
for i in range(2,100):
    for j in range(2,(i//2)+1):
        if i % j ==0:
            break
    else:
        print(i)

