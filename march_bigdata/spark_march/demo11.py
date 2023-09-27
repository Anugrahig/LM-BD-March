# 1 to 10 RDD
# Then find Square

from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.parallelize([i for i in range(1,11)])
rdd1=rdd.map(lambda x:x**2)
rdd1.foreach(print)