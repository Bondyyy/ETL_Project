from databases.mySqlConnect import MySQLConnect
from config.databaseConfig import getDatabaseConfig
from databases.schema_manager import create_mysql_schema, validate_mysql_schema, create_mongodb_schema, validate_mongodb_schema
from databases.mongoDBConnect import MongoDBConnect

def main(config):
    with MySQLConnect(config['mysql'].host, config['mysql'].port, 
                 config['mysql'].user, config['mysql'].password) as mySqlConnect:
        connection, cursor = mySqlConnect.connection, mySqlConnect.cursor
        create_mysql_schema(connection, cursor)
        cursor.execute('INSERT INTO users (user_id, login, gravatar_id, url, avatar_url) VALUES (%s, %s, %s, %s, %s)', 
                       (1, 'demo', '', 'https://demo.com', 'https://demo.com/avatar.com'))
        cursor.execute('INSERT INTO repositories (repo_id, name, url) VALUES (%s, %s, %s)', (1, 'demo', 'https://demo.com'))
        connection.commit() 
        validate_mysql_schema(cursor)

    with MongoDBConnect(config['mongodb'].uri, config['mongodb'].db_name) as mongo_client:
        create_mongodb_schema(mongo_client)
        mongo_client.users.insert_one(
            {'user_id': 1, 'login': 'demo', 'gravatar_id': '', 'url': 'https://demo.com', 'avatar_url': 'https://demo.com/avatar.com'}
        )
        print("Data inserted into MongoDB database successfully")
        validate_mongodb_schema(mongo_client)
        

if __name__ == "__main__":
    config = getDatabaseConfig()
    main(config)