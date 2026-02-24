from dotenv import load_dotenv
import os
from dataclasses import dataclass   

@dataclass
class MySQLConfig:
    host: str
    port: int
    user: str
    password: str
    database: str
    table: str = 'users'

@dataclass
class MongoDBConfig:
    uri: str
    db_name: str

def getDatabaseConfig():
    load_dotenv()  
    config = {
        "mysql": MySQLConfig(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT")),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
        ),
        "mongodb": MongoDBConfig(
            uri=os.getenv("MONGODB_URI"),
            db_name=os.getenv("MONGODB_DB_NAME")
        )
    } 
    return config

def getSparkConfig():
    db_config = getDatabaseConfig()
    spark_config = {
        "mysql":{
            'table': db_config['mysql'].table,
            "jdbc_url": f"jdbc:mysql://{db_config['mysql'].host}:{db_config['mysql'].port}/{db_config['mysql'].database}",
            "config":{
                "host": db_config['mysql'].host,
                "port": db_config['mysql'].port,
                "user": db_config['mysql'].user,
                "password": db_config['mysql'].password,
                "database": db_config['mysql'].database
            }
        },
        "mongodb":{},
        "redis":{}
    }
    return spark_config


if __name__ == "__main__":
    spark_config = getSparkConfig()
    print(spark_config)
