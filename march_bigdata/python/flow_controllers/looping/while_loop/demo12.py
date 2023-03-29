# lower to upper sum of odd and even numbers

lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))
e_sum=0
o_sum=0
while lower <= upper:
    if lower % 2 == 0:
        e_sum = e_sum+lower
    else:
        o_sum = o_sum+lower
    lower += 1
print("Odd Sum =",o_sum)
print("Even Sum =",e_sum)

