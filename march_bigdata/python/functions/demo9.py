# create a simple calculator
# 1.Addition
# 2.Subtraction
# 3. Multiplication
# 4. Division

# num1:
# num2:

# Enter your choice:



# def calculator(c,n1,n2):
#     if(c==1):
#         return n1+n2
#     elif c==2:
#         return n1-n2
#     elif c==3:
#         return  n1//n2
#     else:
#         return n1*n2
#
def addition(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1//n2

def mul(n1,n2):
    return n1*n2

print("1. Addition \n")
print("2. Subtraction \n")
print("1. Division \n")
print("1. Multiplication \n")

c= int(input("Enter your choice: "))
n1=int(input("Enetr number 1 : "))
n2=int(input("Enetr number 2 : "))
if(c==1):
    print(addition(n1,n2))
elif(c==2):
    print(sub(n1,n2))
elif(c==3):
    print(div(n1,n2))
else:
    print(mul(n1,n2))






