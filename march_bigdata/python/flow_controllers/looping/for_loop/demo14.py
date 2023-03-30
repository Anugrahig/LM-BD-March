# check given num is prime number or not
num=int(input("Enter the number : "))
is_prime=0
# con=int(num*0.5)
# print(con)
if num <2:
    is_prime=1
for i in range(2,(num//2)+1):
    # print(i)
    # print(num)
    if num%i ==0 :
        is_prime=1
        break
    else:
        is_prime=0


if is_prime==0:
    print("Prime number ")
else:
    print("Not Prime number ")