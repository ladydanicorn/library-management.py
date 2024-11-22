from book import Book
from user import User
from author import Author
from db_config import DatabaseConnection

def main_menu():
    print("\nWelcome to the Library Management System with Database Integration!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def book_operations():
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Select an option: ")

    if choice == "1":
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT id, name FROM authors")
            authors = cursor.fetchall()
            
            if not authors:
                print("No authors available. Please add an author first.")
                return
            
            print("\nAvailable Authors:")
            for author in authors:
                print(f"ID: {author['id']} - Name: {author['name']}")
        
        title = input("\nTitle: ")
        author_id = input("Enter Author ID from the list above: ")
        try:
            author_id = int(author_id)
            author_exists = False
            for author in authors:
                if author['id'] == author_id:
                    author_exists = True
                    break
            
            if not author_exists:
                print("Error: Invalid author ID. Please select from the available authors or add author in Author Operations.")
                return

        except ValueError:
            print("Error: Author ID must be a number.")
            return        
        isbn = input("ISBN: ")
        publication_date = input("Publication Date (YYYY-MM-DD): ")
        
        try:
            book = Book(title, int(author_id), isbn, publication_date)
            book.save_to_db()
            print(f"Book '{title}' added successfully.")
        except ValueError:
            print("Invalid author ID. Please enter a valid number.")
        except Exception as e:
            print(f"Error adding book: {e}")

    elif choice == "2":
        with DatabaseConnection() as cursor:
            cursor.execute("SELECT * FROM books WHERE availability = TRUE")
            available_books = cursor.fetchall()
            
            if not available_books:
                print("No books available for borrowing.")
                return
            
            print("\nAvailable Books:")
            for book in available_books:
                print(f"ID: {book['id']} - Title: {book['title']}")

        book_id = input("\nEnter book ID from the list above: ")

        with DatabaseConnection() as cursor:
            cursor.execute("SELECT id, name, library_id FROM users")
            users = cursor.fetchall()
            
            if not users:
                print("No users registered in the system. Please add a user first.")
                return
            
            print("\nRegistered Users:")
            for user in users:
                print(f"ID: {user['id']} - Name: {user['name']} (Library ID: {user['library_id']})")

        user_id = input("\nEnter user ID from the list above: ")

        try:
            book_id = int(book_id)
            user_id = int(user_id)

            book_exists = False
            for book in available_books:
                if book['id'] == book_id:
                    book_exists = True
                    break
            if not book_exists:
                print("Error: Invalid book ID. Please select from the available books.")
                return

            user_exists = False
            for user in users:
                if user['id'] == user_id:
                    user_exists = True
                    break
            if not user_exists:
                print("Error: Invalid user ID. Please select from the registered users.")
                return

            with DatabaseConnection() as cursor:
                cursor.execute("SELECT * FROM books WHERE id = %s AND availability = TRUE", (book_id,))
                book = cursor.fetchone()
                if book:
                    book_obj = Book(
                        title=book['title'],
                        author_id=book['author_id'],
                        isbn=book['isbn'],
                        publication_date=book['publication_date'],
                        is_borrowed=not book['availability'],
                        id=book['id']
                    )
                    if book_obj.borrow_book(user_id):
                        print("Book borrowed successfully.")
                    else:
                        print("Failed to borrow book.")
                else:
                    print("Book not available for borrowing.")

        except ValueError:
            print("Error: Book ID and User ID must be numbers.")

    elif choice == "3":
        book_id = input("Enter book ID: ")
        with DatabaseConnection() as cursor:
            cursor.execute("""
                UPDATE borrowed_books SET return_date = CURDATE()
                WHERE book_id = %s AND return_date IS NULL""", (book_id,))
            cursor.execute("UPDATE books SET availability = TRUE WHERE id = %s", (book_id,))
            print("Book returned successfully.")

    elif choice == "4":
        search_term = input("Enter book title or ISBN: ")
        books = Book.search_books(search_term)
        if books:
            for book in books:
                print(f"\nID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author_name']}")
                print(f"ISBN: {book['isbn']}")
                print(f"Status: {'Available' if book['availability'] else 'Borrowed'}")
        else:
            print("No books found.")

    elif choice == "5":
        books = Book.load_from_db()
        if books:
            for book in books:
                print(f"\nID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"ISBN: {book['isbn']}")
                print(f"Status: {'Available' if book['availability'] else 'Borrowed'}")
        else:
            print("No books in the library.")

def user_operations():
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Name: ")
        library_id = input("Library ID: ")
        user = User(name, library_id)
        user.save_to_db()
        print(f"User '{name}' added successfully.")

    elif choice == "2":
        library_id = input("Enter Library ID: ")
        user = User.get_user_details(library_id)
        if user:
            print(f"\nName: {user['name']}")
            print(f"Library ID: {user['library_id']}")
            if user['borrowed_books']:
                print("Borrowed Books:")
                books = user['borrowed_books'].split(',')
                dates = user['borrow_dates'].split(',')
                for book, date in zip(books, dates):
                    print(f"- {book} (Borrowed: {date})")
        else:
            print("User not found.")

    elif choice == "3":
        users = User.load_from_db()
        if users:
            for user in users:
                print(f"\nID: {user['id']}")
                print(f"Name: {user['name']}")
                print(f"Library ID: {user['library_id']}")
                if user['borrowed_books']:
                    print("Borrowed Books:", user['borrowed_books'])
        else:
            print("No users registered.")

def author_operations():
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Author's Name: ")
        biography = input("Biography: ")
        author = Author(name, biography)
        author.save_to_db()
        print(f"Author '{name}' added successfully.")

    elif choice == "2":
        author_id = input("Enter Author ID: ")
        author = Author.get_author_details(author_id)
        if author:
            print(f"\nName: {author['name']}")
            print(f"Biography: {author['biography']}")
            if author['books']:
                print("Books:", author['books'])
        else:
            print("Author not found.")

    elif choice == "3":
        authors = Author.load_from_db()
        if authors:
            for author in authors:
                print(f"\nID: {author['id']}")
                print(f"Name: {author['name']}")
                print(f"Biography: {author['biography']}")
        else:
            print("No authors in the system.")

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