from db_config import DatabaseConnection

class Book:
    def __init__(self, title, author_id, isbn, publication_date, is_borrowed=False, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.is_borrowed = is_borrowed

    def save_to_db(self):
        with DatabaseConnection() as cursor:
            sql = """INSERT INTO books (title, author_id, isbn, publication_date, availability) 
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (self.title, self.author_id, self.isbn, self.publication_date, not self.is_borrowed))

    @staticmethod
    def load_from_db():
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM books")
            return cursor.fetchall()

    def borrow_book(self, user_id):
        if not self.is_borrowed:
            with DatabaseConnection() as cursor:
                cursor.execute("""
                    INSERT INTO borrowed_books (user_id, book_id, borrow_date) 
                    VALUES (%s, %s, CURDATE())""", (user_id, self.id))
                cursor.execute("UPDATE books SET availability = FALSE WHERE id = %s", (self.id,))
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            with DatabaseConnection() as cursor:
                cursor.execute("""
                    UPDATE borrowed_books 
                    SET return_date = CURDATE()
                    WHERE book_id = %s 
                    AND return_date IS NULL""", (self.id,))
                cursor.execute("UPDATE books SET availability = TRUE WHERE id = %s", (self.id,))
            self.is_borrowed = False
            return True
        return False

    @staticmethod
    def search_books(search_term):
        with DatabaseConnection() as cursor:
            cursor.execute("""
                SELECT b.*, a.name as author_name 
                FROM books b
                JOIN authors a ON b.author_id = a.id
                WHERE b.title LIKE %s OR b.isbn = %s""", 
                (f"%{search_term}%", search_term))
            return cursor.fetchall()