# element ==>console check element present in list not using in
# Linear search : we need to compare each element with the input value
# time complexity is high
inp = int(input("Enter an value : "))
lst =[5,15,25,30,35,45,60,70,100,150,120,110,75]
pre=0
for i in lst:
    if i == inp:
        pre=1
        break
if pre==1:
    print("Element is Present ")
else:
    print("Element is not Present ")

