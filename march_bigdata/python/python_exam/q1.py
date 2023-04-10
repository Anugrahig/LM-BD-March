# Palindrome String

strs=input("Enter a String : ")
rev=""
for i in strs:
    rev=i+rev

if strs == rev:
    print("Given string,",strs," is Palindrome ")
else:
    print("Given string is",strs," not Palindrome ")


