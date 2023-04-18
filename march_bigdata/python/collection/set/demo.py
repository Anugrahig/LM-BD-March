# Set

# 1. How to define
# set function is used to define an empty function
st={} # it is an empty dictionary

print(type(st))
st={1,2,3,4,5}
print(type(st))
st1=set()
print(type(st1)) # empty set

# 2. It supports Heterogeneous Data
st={1,2,3,0,"bigdata","python",4,False,123456789,0.0564,3,2}
print(st)
print(type(st))



# 3. Insertion order is not preserved

# 4. It not supports duplicate values

st={10,10,20,30,40,30,30,40,20}
print(st)


st={0,1,True,False}
print(st) # it doesn't support duplicate values

st={True,False,1,0}
print(st)

# 5. Set is mutable
st={10,20,30,40,50,10}
print(st)