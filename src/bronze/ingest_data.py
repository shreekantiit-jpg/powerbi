from src.common.spark_session import get_spark

spark = get_spark()

customers = spark.read \
    .option("header",True) \
    .csv("datasets/customers.csv")

products = spark.read \
    .option("header",True) \
    .csv("datasets/products.csv")

orders = spark.read \
    .option("header",True) \
    .csv("datasets/orders.csv")

customers.write.mode("overwrite") \
    .parquet("bronze/customers")

products.write.mode("overwrite") \
    .parquet("bronze/products")

orders.write.mode("overwrite") \
    .parquet("bronze/orders")

print("Bronze Layer Completed")

spark.stop()