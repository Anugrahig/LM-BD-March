# even count and odd count

lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))
e_count=1
o_count=1
for i in range(lower,upper+1):
    if i % 2 ==0:
        e_count+=1
    else:
        o_count+=1
print("Odd Numbers Count =",o_count-1)
print("Even Numbers Count =",e_count-1)


