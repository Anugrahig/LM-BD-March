# lower to upper even sum and odd sum

#
lower=int(input("Enter the lower limit : "))
upper=int(input("Enter the upper limit : "))
o_sum=0
e_sum=0
for i in range(lower,upper):
    if i%2 == 0:
        e_sum+=i
    else:
        o_sum+=i
print("Even sum =",e_sum)
print("Odd sum =",o_sum)


