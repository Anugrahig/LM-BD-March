# method 3:
# 1 t0 50 even square odd numbers

# [print1 if condition1 else print2 range]

# [print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

lst=[i**2 if i%2==0 else i for i in range(1,51)]
print(lst)