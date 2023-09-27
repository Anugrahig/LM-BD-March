# 1to 40 even numbers

from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.parallelize([i for i in range(1,41) if i%2==0])
rdd.foreach(print)