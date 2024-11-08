from book import Book
from user import User
from author import Author

def main_menu():
    print("\nWelcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def book_operations():
    books = Book.load_from_file()
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Select an option: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        publication_date = input("Publication Date: ")
        book = Book(title, author, genre, publication_date)
        book.save_to_file()
        print(f"Book '{title}' added successfully.")

    elif choice == "2":
        book_title = input("Enter book title to borrow: ")
        for book in books:
            if book.get_details()["title"] == book_title and book.borrow_book():
                print(f"{book_title} borrowed.")
                break
        else:
            print("Book not available for borrowing.")

def user_operations():
    users = User.load_from_file()
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Name: ")
        library_id = input("Library ID: ")
        user = User(name, library_id)
        user.save_to_file()
        print(f"User '{name}' added successfully.")

def author_operations():
    authors = Author.load_from_file()
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Author's Name: ")
        biography = input("Biography: ")
        author = Author(name, biography)
        author.save_to_file()
        print(f"Author '{name}' added successfully.")

def run():
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run()
