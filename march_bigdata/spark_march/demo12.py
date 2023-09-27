# 1 to 30 element RDD 1->even,2->odd,,,

from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.parallelize([i for i in range(1,31) ])
# pair rdd
rdd1=rdd.map(lambda x:(x,"even") if x%2==0  else (x,"odd"))
rdd1.foreach(print)