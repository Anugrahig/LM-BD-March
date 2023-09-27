from  pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("./sample.txt")
rdd.foreach(print)