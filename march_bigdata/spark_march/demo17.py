# a yes ,a not present print no
from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("./sample.txt")
rdd1=rdd.map(lambda x: "yes" if "a" in x else "no" )
rdd1.foreach(print)