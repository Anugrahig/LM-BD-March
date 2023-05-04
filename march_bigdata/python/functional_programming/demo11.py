# 1 to 50 odd numbers print numbers square

lst=[i**2 for i in range(1,51) if i%2==1]
print(lst)

# 1 to 30 even numbers qube
lst= [ (i,i**3) for i in range(1,31) if i%2==0]
print(lst)

# print vowels in a using list comprehension
string="luminartechnolab"
lst=[i for i in string if i in "aeiou"]
print(lst)

# print number of consoants in a string

lst=len([i for i in string if i not in "aeiou" ])
# print(len(lst))
print(lst)