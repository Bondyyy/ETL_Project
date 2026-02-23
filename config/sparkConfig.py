from pyspark.sql import SparkSession
from typing import Optional, List, Dict


class SparkConnect:
    def __init__(self, 
                 app_name: str = 'ETL Pipeline', 
                 master: str = 'local[*]',
                 executor_memory: Optional[str] = '4g',
                 executor_cores: Optional[int] = 2,
                 driver_memory: Optional[str] = '2g',
                 num_executors: Optional[int] = 2,
                 jar_packages: Optional[List[str]] = None,
                 spark_config: Optional[Dict[str, str]] = None,
                 log_level: str = 'INFO'):
        self.app_name = app_name
        
        self.spark = self.create_spark_session(master, executor_memory, executor_cores, driver_memory, 
                                               num_executors, jar_packages, spark_config, log_level)

    def create_spark_session(self,
                             master: str = 'local[*]',
                             executor_memory: Optional[str] = '4g',
                             executor_cores: Optional[int] = 2,
                             driver_memory: Optional[str] = '2g',
                             num_executors: Optional[int] = 2,
                             jar_packages: Optional[List[str]] = None,
                             spark_config: Optional[Dict[str, str]] = None,
                             log_level: str = 'INFO') -> SparkSession:
        
        builder =  SparkSession.builder.appName(self.app_name).master(master)

        if executor_memory:
            builder.config('spark.executor.memory', executor_memory)
        if executor_cores:
            builder.config('spark.executor.cores', executor_cores)
        if driver_memory:
            builder.config('spark.driver.memory', driver_memory)
        if num_executors:
            builder.config('spark.executor.instances', num_executors)
        
        if jar_packages:
            jar_path = ",".join([j.strip() for j in jar_packages])
            builder.config('spark.jars.packages', jar_path)
        
        if spark_config:
            for key, value in spark_config.items():
                builder.config(key, value)
        
        spark = builder.getOrCreate()

        spark.sparkContext.setLogLevel(log_level)
        print(f"Spark session created with app name '{self.app_name}' and master '{master}'")
        return spark


    def stop(self):
        if self.spark:
            self.spark.stop()
            print("Spark session stopped successfully")
                
        