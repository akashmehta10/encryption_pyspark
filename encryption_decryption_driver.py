from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import functions as F
from encryption_library.encryption_lib import udf_decrypt, udf_encrypt

conf = SparkConf()
conf.set("set hive.vectorized.execution", "true")
conf.set("set hive.vectorized.execution.enabled", "true")
conf.set("set hive.cbo.enable", "true")
conf.set("set hive.compute.query.using.stats", "true")
conf.set("set hive.stats.fetch.column.stats", "true")
conf.set("set hive.stats.fetch.partition.stats", "true")
conf.set('spark.sql.shuffle.partitions', 500)

spark = SparkSession.builder.appName("spark_encryption_decryption").config(conf=conf).enableHiveSupport().getOrCreate()

# 32 bytes secretKey
secretkey = '5ad8f52071d25165e7e68064ab194ec2'
schema = StructType([
    StructField(name='id',
                dataType=StringType(),
                nullable=False),
    StructField(name='name',
                dataType=StringType(), nullable=False),
    StructField(name='message',
                dataType=StringType(), nullable=False)
])

data1 = [
    ('1', 'John', 'Do you even lift?'),
    ('2', 'Adam', 'Do you like Wendy\'s?'),
    ('3', 'Thomas', 'The great state of Texas!')
]
df1 = spark.createDataFrame (data=data1, schema=schema)
df1.cache()
df1.show(10, False)
secretKey = '5ad8f52071d25165e7e68064ab194ec2'

#Encrypt single column
df2 = df1.withColumn("encrypted_message", udf_encrypt(secretKey)(F.col('message')))
df2.show(10, False)
df2.cache()
df3 = df2.withColumn("decrypted_message", udf_decrypt(secretKey)(F.col('encrypted_message')))
df3.show(10, False)

#Encrypt all/multiple columns at once
# Chose separator ":%%%:"

ignored_columns = ["id"]
cols = list(set(df1.columns) - set(ignored_columns))
columns = [F.col(column) for column in cols]

df4 = df1.withColumn("concat_col", F.concat_ws(":%%%:", *columns))
df4.show(10, False)
df5 = df4.withColumn("encrypted_concat_col", udf_encrypt(secretKey)(F.col('concat_col')))
df5.show(10, False)
df5.cache()
df6 = df5.withColumn("decrypted_concat_col", udf_decrypt(secretKey)(F.col('encrypted_concat_col')))
df6.show(10, False)