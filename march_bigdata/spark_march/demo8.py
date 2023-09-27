# customer file to RDD

from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("/home/anugrah/Downloads/Hadoopfiles/customer")
rdd.foreach(print)