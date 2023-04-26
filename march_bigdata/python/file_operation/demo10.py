
# write file in another file
f=open("sample5","r")
w=open("sample6","w")
for i in f:
    w.write(i)
