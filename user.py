import json
from datetime import datetime, timedelta

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = {}  
        self.__reserved_books = []

    def borrow_book(self, book_title):
        due_date = datetime.now() + timedelta(days=14)
        self.__borrowed_books[book_title] = due_date
        print(f"{book_title} borrowed until {due_date.strftime('%Y-%m-%d')}")

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            due_date = self.__borrowed_books.pop(book_title)
            overdue_days = (datetime.now() - due_date).days
            if overdue_days > 0:
                fine = overdue_days * 0.5  
                print(f"Overdue by {overdue_days} days. Fine: ${fine:.2f}")
            print(f"{book_title} returned successfully.")
        else:
            print(f"{book_title} was not borrowed by this user.")

    def reserve_book(self, book_title):
        if book_title not in self.__reserved_books:
            self.__reserved_books.append(book_title)
            return f"{book_title} has been reserved."
        return f"{book_title} is already reserved by you."

    def get_details(self):
        return {
            "name": self.__name,
            "library_id": self.__library_id,
            "borrowed_books": self.__borrowed_books,
            "reserved_books": self.__reserved_books
        }

    def save_to_file(self):
        user_data = self.get_details()
        with open("users.txt", "a") as file:
            file.write(json.dumps(user_data) + "\n")

    @staticmethod
    def load_from_file():
        users = []
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    user_data = json.loads(line.strip())
                    user = User(
                        name=user_data["name"],
                        library_id=user_data["library_id"]
                    )
                    user.__borrowed_books = user_data["borrowed_books"]
                    user.__reserved_books = user_data["reserved_books"]
                    users.append(user)
        except FileNotFoundError:
            print("No users file found.")
        return users
