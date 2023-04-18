# Tuples
# 1. How to define

tu=()
print(type(tu))
# using tuple function
tu1 = tuple()
print(type(tu1))

# 2. It supports Heterogeneous
tu=(10,10.5,"bigdata","luminar",True,1234567890)
print(tu)

# 3.It support Duplicate values
tu=(12,12,3,"luminar","luminar",3,150.5)
print(tu)

# 4. Insertion order is preserved

# 5.Immutable (values cannot be change)
tu=(10,20,30,40,50,60,70,80,90,100)
tu[2]=200
print(tu)


