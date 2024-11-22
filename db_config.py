import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='library_db',
                user='root',
                password='Pikapika07$'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()