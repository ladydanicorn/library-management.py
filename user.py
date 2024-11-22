import json
from db_config import DatabaseConnection
from datetime import datetime, timedelta

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def save_to_db(self):
        with DatabaseConnection() as cursor:
            sql = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(sql, (self.name, self.library_id))

    @staticmethod
    def load_from_db():
        with DatabaseConnection() as cursor:
            cursor.execute("""
                SELECT u.*, 
                       GROUP_CONCAT(b.title) as borrowed_books
                FROM users u
                LEFT JOIN borrowed_books bb ON u.id = bb.user_id
                LEFT JOIN books b ON bb.book_id = b.id
                GROUP BY u.id""")
            return cursor.fetchall()

    @staticmethod
    def get_user_details(library_id):
        with DatabaseConnection() as cursor:
            cursor.execute("""
                SELECT u.*, 
                       GROUP_CONCAT(b.title) as borrowed_books,
                       GROUP_CONCAT(bb.borrow_date) as borrow_dates
                FROM users u
                LEFT JOIN borrowed_books bb ON u.id = bb.user_id
                LEFT JOIN books b ON bb.book_id = b.id
                WHERE u.library_id = %s
                GROUP BY u.id""", (library_id,))
            return cursor.fetchone()