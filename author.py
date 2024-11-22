import json

from db_config import DatabaseConnection

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def save_to_db(self):
        with DatabaseConnection() as cursor:
            sql = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(sql, (self.name, self.biography))

    @staticmethod
    def load_from_db():
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM authors")
            return cursor.fetchall()

    @staticmethod
    def get_author_details(author_id):
        with DatabaseConnection() as cursor:
            cursor.execute("""
                SELECT a.*, GROUP_CONCAT(b.title) as books
                FROM authors a
                LEFT JOIN books b ON a.id = b.author_id
                WHERE a.id = %s
                GROUP BY a.id""", (author_id,))
            return cursor.fetchone()
