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
                book.save_to_file()
                print(f"{book_title} borrowed successfully.")
                break
        else:
            print("Book not available for borrowing.")

    elif choice == "3":
        book_title = input("Enter book title to return: ")
        for book in books:
            if book.get_details()["title"] == book_title and book.return_book():
                book.save_to_file()
                print(f"{book_title} returned successfully.")
                break
        else:
            print("Book return failed. Book may not be borrowed or doesn't exist.")

    elif choice == "4":
        search_title = input("Enter book title to search: ")
        found = False
        for book in books:
            details = book.get_details()
            if details["title"].lower() == search_title.lower():
                print("\nBook found:")
                print(f"Title: {details['title']}")
                print(f"Author: {details['author']}")
                print(f"Genre: {details['genre']}")
                print(f"Publication Date: {details['publication_date']}")
                print(f"Status: {'Borrowed' if details['is_borrowed'] else 'Available'}")
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "5":
        if not books:
            print("No books in the library.")
        else:
            print("\nAll Books:")
            for book in books:
                details = book.get_details()
                print(f"\nTitle: {details['title']}")
                print(f"Author: {details['author']}")
                print(f"Genre: {details['genre']}")
                print(f"Publication Date: {details['publication_date']}")
                print(f"Status: {'Borrowed' if details['is_borrowed'] else 'Available'}")

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

    elif choice == "2":
        library_id = input("Enter Library ID: ")
        found = False
        for user in users:
            details = user.get_details()
            if details["library_id"] == library_id:
                print("\nUser Details:")
                print(f"Name: {details['name']}")
                print(f"Library ID: {details['library_id']}")
                print("Borrowed Books:")
                for book, due_date in details["borrowed_books"].items():
                    print(f"- {book} (Due: {due_date})")
                print("Reserved Books:")
                for book in details["reserved_books"]:
                    print(f"- {book}")
                found = True
                break
        if not found:
            print("User not found.")

    elif choice == "3":
        if not users:
            print("No users registered.")
        else:
            print("\nAll Users:")
            for user in users:
                details = user.get_details()
                print(f"\nName: {details['name']}")
                print(f"Library ID: {details['library_id']}")
                print(f"Number of borrowed books: {len(details['borrowed_books'])}")
                print(f"Number of reserved books: {len(details['reserved_books'])}")

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

    elif choice == "2":
        author_name = input("Enter author name: ")
        found = False
        for author in authors:
            details = author.get_details()
            if details["name"].lower() == author_name.lower():
                print("\nAuthor Details:")
                print(f"Name: {details['name']}")
                print(f"Biography: {details['biography']}")
                found = True
                break
        if not found:
            print("Author not found.")

    elif choice == "3":
        if not authors:
            print("No authors in the system.")
        else:
            print("\nAll Authors:")
            for author in authors:
                details = author.get_details()
                print(f"\nName: {details['name']}")
                print(f"Biography: {details['biography']}")

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