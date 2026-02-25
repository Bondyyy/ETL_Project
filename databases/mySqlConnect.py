import mysql.connector
from mysql.connector import Error


class MySQLConnect:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.config = {
            'host': self.host,
            'port': self.port,  
            'user': self.user,
            'password': self.password
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        try:   
            self.connection = mysql.connector.connect(**self.config )
            self.cursor = self.connection.cursor()
            print("------------Connected to MySQL database------------")
        except Error as e:
            raise Exception(f"----------Error connecting to MySQL database: {e}-----------------") 
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("--------------Disconnected from MySQL database--------------")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()