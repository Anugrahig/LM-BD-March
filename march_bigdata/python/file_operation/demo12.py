# copy file without apple fuits
f=open("sample7","r")
w=open("sample7_copy","w")
for i in f:
    data=i.rstrip("\n")
    if data=="apple":
        continue
    else:
        w.write(data)
        w.write("\n")

