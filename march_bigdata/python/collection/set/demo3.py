# Set Operation

# 1.Union
# 2.Intersection
# 3.Difference

st1={1,2,3,4,5,6,7,8,9,10}
st2={6,7,8,9,10,11,12,13,14,15}
# union
# combine both set
st3=st1.union(st2)
print(st3)
# intersection
# common elements in both set
st4=st1.intersection(st2)
print(st4)

# difference
# A-B
st5= st1.difference(st2)
# B-A
st6=st2.difference(st1)
print(st5)
print(st6)

