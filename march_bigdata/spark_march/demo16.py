from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.textFile("./sample.txt")
rdd.foreach(print)
print("*"*100)
rdd1=rdd.map(lambda x:x.startswith("M"))
rdd1.foreach(print)