from databases.mySqlConnect import MySQLConnect
from config.databaseConfig import getDatabaseConfig
from databases.schema_manager import create_mysql_schema

def main(config):
    with MySQLConnect(config['mysql'].host, config['mysql'].port, 
                 config['mysql'].user, config['mysql'].password) as mySqlConnect:
        connection, cursor = mySqlConnect.connection, mySqlConnect.cursor
        create_mysql_schema(connection, cursor)

if __name__ == "__main__":
    config = getDatabaseConfig()
    main(config)