# map operation in RDD
from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.parallelize([i for i in range(1,21)])
nw_rdd=rdd.map(lambda x:x+2)
nw_rdd.foreach(print)