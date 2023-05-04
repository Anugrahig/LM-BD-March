# assignment question
"""
Find all of the numbers from 1–1000 that are divisible by 8
Find all of the numbers from 1–1000 that have a 6 in them
Count the number of spaces in a string (use string above)
Remove all of the vowels in a string (use string above)
Find all of the words in a string that are less than 5 letters (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
"""
string = "Practice Problems to Drill List Comprehension in Your Head"
lst1=[i for i in range(1,1000) if i%8==0]
print(lst1)

lst5=[ i for i in lst1 if "6" in str(i) ]
print(lst5)

lst2=[i for i in string if i==" " ]
print(len(lst2))

lst3=[i for i in string if i not in "aeiouAEIOU"]
print("".join(lst3))

lst4=[ i for i in string.split() if len(i)<=5]
print(lst4)
# print(string)
# for i in string:
    # print(i.strip(" "))
