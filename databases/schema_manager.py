from pathlib import Path

SQL_FILE_PATH = Path(__file__).parent.parent / 'sql' / 'schema.sql'

def create_mysql_schema(connection, cursor):
    database = 'github_data'

    cursor.execute(f"DROP DATABASE IF EXISTS {database}") 
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    connection.commit()
    print(f'Database {database} created successfully')

    connection.database = database

    with open(SQL_FILE_PATH, 'r') as sql_file:
        sql_script = sql_file.read()
        sql_commands = sql_script.split(';')
        for command in sql_commands:
            command = command.strip()
            if command:
                cursor.execute(command)
    print('Schema created successfully')

def validate_mysql_schema(cursor):
    cursor.execute('SHOW TABLES')
    # print(cursor.fetchall())
    listTable = cursor.fetchall()
    for table in listTable:
        if 'users' not in table[0] and 'repositories' not in table[0]:
            raise ValueError(f"Table {table} not found in database")
    print('Schema validated successfully')
    
    cursor.execute('''
                   SELECT * FROM users 
                   WHERE user_id = 1
                   ''')
    user = cursor.fetchone()
    if user is None:
        raise ValueError('User not found in users table')
    print('User found in users table')

    cursor.execute('''
                   SELECT * FROM repositories 
                   WHERE repo_id = 1
                   ''')
    repository = cursor.fetchone()
    if repository is None:
        raise ValueError('Repository not found in repositories table')
    print('Repository found in repositories table')