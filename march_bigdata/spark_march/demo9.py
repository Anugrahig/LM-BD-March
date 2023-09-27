# sample4.txt to Rdd
from pyspark import  SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("/home/anugrah/Downloads/Hadoopfiles/sample4.txt")
rdd.foreach(print)