# read 4 sub mark out of 50 1) calculate total 2)Print total 3)
# 180 A+
# 160-179 A
# 140-159 B+
# 120-139 B
# 100-119 C+
# 80-99 C
# Below F

sub1= int(input("Enter 1st Subject  Mark Out of 50 : "))
sub2= int(input("Enter 2nd Subject  Mark Out of 50 : "))
sub3= int(input("Enter 3rd Subject  Mark Out of 50 : "))
sub4= int(input("Enter 4th Subject  Mark Out of 50 : "))
total = sub1+sub2+sub3+sub4
print("Total mark of Student is  = ",total)

if total>=180:
    print("A+")
elif(total>=160 and total<=179):
    print("A")
elif(total>=140 and total<=159):
    print("B+")
elif(120<=total<=139):
    print("B")
elif(100<=total<=119):
    print("C+")
elif(80<=total<=99):
    print("C")
else:
    print("Failed")


