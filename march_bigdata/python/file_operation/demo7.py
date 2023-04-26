# year count
# 1930 -199
ycount_dic = {}
f = open("movies_cleaned_pandas.csv", "r")
for i in f:
    data = i.rstrip("\n").split(",")

    if data[2] in ycount_dic:
        ycount_dic[data[2]] += 1
    else:
        ycount_dic[data[2]] = 1
    #     print in b/w 1930 and 1999
    if "1930" < data[2] < "1999":
        print(data)
# Year count
# print(ycount_dic)
for k,v in ycount_dic.items():
    print(f"{k},{v}")
"""
id=0
name=1
year=2
rating=3
len=4
"""
