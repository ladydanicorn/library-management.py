import json

class Book:
    def __init__(self, title, author, genre, publication_date, is_borrowed=False):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = is_borrowed

    def borrow_book(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def get_details(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "genre": self.__genre,
            "publication_date": self.__publication_date,
            "is_borrowed": self.__is_borrowed
        }

    def save_to_file(self):
        book_data = self.get_details()
        with open("books.txt", "a") as file:
            file.write(json.dumps(book_data) + "\n")

    @staticmethod
    def load_from_file():
        books = []
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_data = json.loads(line.strip())
                    book = Book(
                        title=book_data["title"],
                        author=book_data["author"],
                        genre=book_data["genre"],
                        publication_date=book_data["publication_date"],
                        is_borrowed=book_data["is_borrowed"]
                    )
                    books.append(book)
        except FileNotFoundError:
            print("No books file found.")
        return books
