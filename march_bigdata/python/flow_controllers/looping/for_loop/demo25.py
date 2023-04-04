# Pattern Printing : 10
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1


for i in range(1,7):
    for j in range(0+i,1,-1):
        print(j-1,end=" ")
    print()
    # for i in range(1,6):
    # for j in range(i,0,-1):
    #     print(j,end=" ")
    # print()