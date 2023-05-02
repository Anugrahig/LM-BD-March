
# 1*15
# 2*15
# 3*15
# 4*15
# 5*15


def compute(n):
    return lambda x : x*n
for i in range(1,11):
    result=compute(i)
    print(i,"* 17 = ",result(17))

# help(lambda)