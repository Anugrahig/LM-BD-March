# add : insert only one element at a time

st={4,7,3,2}
print(st)
st.add(8)
st.add(1)
# st.add(10,30,50,70) =>error
print(st)

# update : insert more than one values

st.update([12,3,4,5,67,8])
print(st)

# remove element from list
st={4,7,3,2,5,10,25,20}
# remove : delete any element
st.remove(7)
print(st)

# discard  : it also used for delete element in a set
# if deleting element not present in the set it doesn't return error
# but remove return error
st.discard(25)
print(st)
st.discard(28)
print(st)




