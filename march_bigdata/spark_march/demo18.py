# flatMap
# convert 2D to 1D using flatMap
# word by word
from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("./sample.txt")
# rdd.foreach(print)
rdd1=rdd.map(lambda x:x.split(" "))
# result in single step
# rdd1=rdd.flatMap(lambda x:x.split(" "))

# rdd1.foreach(print)
rdd2=rdd1.flatMap(lambda x:x)
rdd2.foreach(print)