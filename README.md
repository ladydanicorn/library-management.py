# Library Management System

## Project Overview
This Library Management System is a command-line application built in Python that demonstrates database integration with MySQL. The system allows librarians and users to manage books, user accounts, and author information efficiently through a persistent database.

## Features
### Book Management
- Add new books to the library
- Track book borrowing status  
- Search for books by title or ISBN
- Display all available books
- Borrow and return books
- Track book availability in real-time

### User Management
- Add new library users
- View user details including borrowed books
- Track user borrowing history
- Display all registered users
- Monitor user's current borrowed books

### Author Management  
- Add new authors
- Store author biographies
- View author details including their books
- Display all authors in the system

## Technical Features
- MySQL Database Integration
- Object-Oriented Design
- Foreign key relationships between tables
- Transaction handling with context managers
- Comprehensive error handling and input validation
- Modular code structure with separate classes
- Real-time data persistence
- Data integrity through foreign key constraints

## Project Structure
### Directory Layout
```
library_mgmt/
    ├── author.py       # Author class implementation
    ├── book.py         # Book class implementation
    ├── user.py         # User class implementation
    ├── library.py      # Main program and menu interface
    ├── db_config.py    # Database configuration and connection handling
    └── schema.sql      # Database schema definitions
```

## Database Schema
### Tables
- books: Stores book information with foreign key to authors
- authors: Stores author information
- users: Stores user information
- borrowed_books: Tracks book borrowing history with foreign keys to books and users

## How to Run
1. Ensure you have Python 3.x installed on your system
2. Install MySQL Server and MySQL Connector for Python:
   ```bash
   pip install mysql-connector-python
   ```
3. Set up the database:
   - Run MySQL Server
   - Create the database and tables using schema.sql
   - Update database credentials in db_config.py
4. Clone this repository to your local machine
5. Navigate to the project directory
6. Run the program using:
   ```bash
   python library.py
   ```

## Features Implemented From Requirements
- MySQL Database Integration
- Enhanced command-line user interface
- Complete class structure (Book, User, Author)
- Database connection handling
- Transaction management
- Input validation
- Foreign key constraint enforcement
- JOIN operations for related data
- Real-time data updates

## System Details

### Classes and Functionality

#### Book Class
- Manages individual book information and status
- Tracks borrowing status in database
- Stores book details (title, author, ISBN, publication date)
- Handles book borrowing and returning operations
- Provides database persistence
- Implements search functionality

#### User Class
- Manages library member information
- Tracks borrowed books through database relations
- Manages user library IDs
- Provides database persistence
- Links users to their borrowed books

#### Author Class
- Stores author information and biographies
- Links authors to their books through foreign keys
- Provides database persistence
- Manages author-book relationships

## Future Enhancements
- Implement more advanced search functionality
- Add unit tests
- Add administrative features
- Implement user authentication
- Add book reservation system
- Add fine calculation for overdue books
- Implement book return deadline tracking

## Author
Danielle Bronson  
Coding Temple 
Date: 2024