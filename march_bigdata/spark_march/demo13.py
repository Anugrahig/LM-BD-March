#1 to 50 range
# 1--15 => small
# 16--40=>medium
# 41--50=>large


from pyspark import SparkContext
sc=SparkContext(master="local",appName="march").getOrCreate()
rdd=sc.parallelize([i for i in range(1,51)])
rdd1=rdd.map(lambda x:("small",x) if x<15 else ("medium",x) if x<40 else ("large",x))
rdd1.foreach(print)