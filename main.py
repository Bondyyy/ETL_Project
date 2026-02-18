from databases.mySqlConnect import MySQLConnect
from config.databaseConfig import getDatabaseConfig

def main(config):
    with MySQLConnect(config['mysql'].host, config['mysql'].port, 
                 config['mysql'].user, config['mysql'].password) as mySqlConnect:
        connection, cursor = mySqlConnect.connection, mySqlConnect.cursor


if __name__ == "__main__":
    config = getDatabaseConfig()
    main(config)