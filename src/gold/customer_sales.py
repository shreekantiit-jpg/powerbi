from src.common.spark_session import get_spark
from pyspark.sql.functions import col

spark = get_spark()

customers = spark.read.parquet(
    "silver/customers"
)

orders = spark.read.parquet(
    "bronze/orders"
)

products = spark.read.parquet(
    "bronze/products"
)

sales = orders.join(
    customers,
    "customer_id"
).join(
    products,
    "product_id"
)

sales = sales.withColumn(
    "revenue",
    col("quantity").cast("int") *
    col("price").cast("int")
)

sales.write.mode("overwrite") \
    .csv("gold/customer_sales",
         header=True)

sales.show()

print("Gold Layer Completed")

spark.stop()