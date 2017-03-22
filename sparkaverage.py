from pyspark import SparkConf, SparkContext
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

#average
nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 20])
nums.collect()
sumAndCount = nums.map(lambda x: (x, 1)).fold((0, 0), (lambda x, y: (x[0] + y[0], x[1] + y[1])))
sumAndCount

avg = float(sumAndCount[0]) / float(sumAndCount[1])
avg

#filter

nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
nums.collect()


filtered1 = nums.filter(lambda x : x % 2 == 1)
filtered1.collect()


filtered2 = nums.filter(lambda x : x % 2 == 0)
filtered2.collect()
