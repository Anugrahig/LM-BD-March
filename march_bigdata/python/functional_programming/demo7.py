lst=[1,2,3,4,5,6,7,8,9,10]
# without lambda function
"""def square(n):
    return  n**n

lst1=list(map(square,lst))
print(lst1)"""

lst1=list(map(lambda num:num**2,lst))
print(lst1)

# filter

lst1=list(filter(lambda x: x%2==0,lst))
print(lst1)
# find odd number in a list and print qubes
lst1= list(filter(lambda num:num%2==1,lst))
lst2=list(map(lambda num:num**3,lst1))
# map and filter in a single line
lst3=list(map(lambda n:n**3,filter(lambda n:n%2==1,lst )))
print(lst3)
print(lst2)