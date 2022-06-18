from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Customer').getOrCreate()
dataset = spark.read.csv('file.csv')
dataset.show()
