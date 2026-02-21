from dotenv import load_dotenv
import os
from dataclasses import dataclass   

@dataclass
class MySQLConfig:
    host: str
    port: int
    user: str
    password: str

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
            password=os.getenv("MYSQL_PASSWORD")
        ),
        "mongodb": MongoDBConfig(
            uri=os.getenv("MONGODB_URI"),
            db_name=os.getenv("MONGODB_DB_NAME")
        )
    } 
    return config

if __name__ == "__main__":
    config = getDatabaseConfig()
    for key, value in config.items():
        print(f"{key}: {value}")
