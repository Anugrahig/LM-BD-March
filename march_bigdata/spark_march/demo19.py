
# sample ==> rdd
# word by data
# vowels present or not
from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("./sample.txt")
# rdd.foreach(print)
rdd1=rdd.flatMap(lambda x:x.split(" "))
# rdd1.foreach(print)
vowels="aeiouAEIOU"
rdd2=rdd1.map(lambda x:(x,[ 1 if i in vowels  else 0 for i in x]))
rdd2.foreach(print)

# rdd2=rdd1.map(lambda x:x.split)
# rdd2.foreach(print)

