# lst=[1,2,3,4,5]
#1. create a identical list
#2. create a list from the element of range from 1200 to 2000 withe step of 130
#3. use LC to construct a new list ,but add 6 to each list
#4. using LC , construct list from the seqaure of each element
#5. construct list from the seqaure of each element in the list if the sqaure greater than 15

lst=[1,2,3,4,5]
lst1=[i for i in lst]
print(lst1)
lst2=[i for i in range(1200,2000,130)]
print(lst2)
lst3=[i+6 for i in lst1]
print(lst3)
lst4=[i**2 for i in lst1]
print(lst4)
lst5=[ i**2 for i in lst1 if i**2>=15 ]
print(lst5)