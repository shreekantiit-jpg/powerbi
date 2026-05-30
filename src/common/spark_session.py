from pyspark.sql import SparkSession

def get_spark():

    spark = SparkSession.builder \
        .appName("RetailPlatform") \
        .master("local[*]") \
        .getOrCreate()

    return spark