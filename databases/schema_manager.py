from pathlib import Path

SQL_FILE_PATH = Path(__file__).parent.parent / 'sql' / 'schema.sql'
def create_mysql_schema(connection, cursor):
    database = 'github_data'

    cursor.execute(f"DROP DATABASE IF EXISTS {database}")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor.commit()
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