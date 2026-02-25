from config.sparkConfig import SparkConnect
from pyspark.sql.types import *
from pyspark.sql.functions import col
from src.spark.sparkWriteData import SparkWriteDatabases
from config.databaseConfig import getSparkConfig

import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

def main():
    jar_packages = ["mysql:mysql-connector-java:8.0.33",
                    "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"]
    
    spark_connect = SparkConnect(
        app_name='Spark ETL Pipeline',
        master='local[*]',
        executor_memory='4g',
        executor_cores=2,
        driver_memory='2g',
        num_executors=2,
        jar_packages=jar_packages,
        log_level='INFO'
    )

    schema = StructType([
        StructField('actor', StructType([
            StructField('id', IntegerType(), True),
            StructField('login', StringType(), True),
            StructField('gravatar_id', StringType(), True),
            StructField('url', StringType(), True),
            StructField('avatar_url', StringType(), True),
        # StructField('spark_temp', StringType(), True),
        ]), True),
        StructField('repo', StructType([
            StructField('id', LongType(), False),
            StructField('name', StringType(), True),
            StructField('url', StringType(), True),
        ]), True)
    ])

    df = spark_connect.spark.read.schema(schema).json('D:\\ProjectETL\\data\\2015-03-01-17.json')
    df_write_table = df.select(col("actor.id").alias("user_id"), 
                               col("actor.login").alias("login"),
                               col("actor.gravatar_id").alias("gravatar_id"),
                               col("actor.url").alias("url"),
                               col("actor.avatar_url").alias("avatar_url"))
    
    spark_config = getSparkConfig()
    df_write = SparkWriteDatabases(spark_connect.spark, spark_config)
    #df_write.sparkWriteToMySQL(df_write_table, spark_config['mysql']['table'], spark_config['mysql']['jdbc_url'], spark_config['mysql']['config'], mode='append')
    #df_write.sparkWriteToMongoDB(df_write_table, 'users', spark_config['mongodb']['uri'], spark_config['mongodb']['db_name'], mode='append')
    df_write.sparkWriteAllDatabases(df_write_table, mode='overwrite')

    


if __name__ == "__main__":
    main()