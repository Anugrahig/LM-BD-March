# read number from file ,find sum and append to a list

f=open("sample2","r")
lst=[]
for i in f:
    lst.append(int(i.strip("\n")))
print(lst)
print("Sum :",sum(lst))


# rstrip : right strip
# lstrip : left strip
""
stri="hello"
stri2=stri.rstrip("o\n")
print(stri2)
""

