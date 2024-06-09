import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG

class Database:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(**DATABASE_CONFIG)
            return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    @staticmethod
    def close_connection(connection):
        if connection.is_connected():
            connection.close()
