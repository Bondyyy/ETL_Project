from config.sparkConfig import SparkConnect
import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
def main():
    spark_connect = SparkConnect(
        app_name='Spark ETL Pipeline',
        master='local[*]',
        executor_memory='4g',
        executor_cores=2,
        driver_memory='2g',
        num_executors=2,
        log_level='INFO'
    )
    data = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie'], [4, 'David'], [5, 'Eve']]
    df = spark_connect.spark.createDataFrame(data, ['id', 'name'])
    df.show()


if __name__ == "__main__":
    main()