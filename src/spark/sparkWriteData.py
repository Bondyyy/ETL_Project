from pyspark.sql import SparkSession, DataFrame
from typing import Dict

class SparkWriteDatabases:
    def __init__(self, spark: SparkSession, db_config: Dict): 
        self.spark = spark
        self.db_config = db_config
    
    def sparkWriteToMySQL(self, df: DataFrame, table_name: str, jdbc_url: str, config: Dict, mode: str = 'append'):
        df.write.format('jdbc') \
            .option('url', jdbc_url) \
            .option('dbtable', table_name) \
            .option('user', config['user']) \
            .option('password', config['password']) \
            .option('driver', 'com.mysql.cj.jdbc.Driver') \
            .mode(mode) \
            .save()
        print(f"--------------Data written to MySQL table '{table_name}' successfully-----------------")

    def sparkWriteToMongoDB(self, df: DataFrame, collection_name: str, uri:  str, db_name: str, mode: str = 'append'):
        df.write.format('com.mongodb.spark.sql.DefaultSource') \
            .option('uri', uri) \
            .option('database', db_name) \
            .option('collection', collection_name) \
            .mode(mode) \
            .save()
        print(f"-----------------Data written to MongoDB collection '{collection_name}' successfully------------------")
    
    def sparkWriteAllDatabases(self, df: DataFrame, mode: str = 'append'):
        self.sparkWriteToMySQL(
            df, 
            self.db_config['mysql']['table'], 
            self.db_config['mysql']['jdbc_url'], 
            self.db_config['mysql']['config'], 
            mode
        )
        self.sparkWriteToMongoDB(
            df, 
            self.db_config['mongodb']['collection'],
            self.db_config['mongodb']['uri'], 
            self.db_config['mongodb']['db_name'], 
            mode
        )
        print("--------------Data written to all databases successfully-----------------")