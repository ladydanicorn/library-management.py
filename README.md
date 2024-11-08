# Library Management System
## By Danielle Bronson
### Coding Temple Project

## Project Overview
This Library Management System is a command-line application built in Python that demonstrates Object-Oriented Programming (OOP) principles. The system allows librarians and users to manage books, user accounts, and author information efficiently.

## Features
### Book Management
- Add new books to the library
- Track book borrowing status  
- Search for books
- Display all available books
- Borrow and return books

### User Management
- Add new library users
- View user details
- Track borrowed books
- Manage book reservations
- Calculate late fees

### Author Management  
- Add new authors
- Store author biographies
- View author details

## Technical Features
- Object-Oriented Design with proper encapsulation using private attributes
- File-based data persistence using JSON format
- Error handling for file operations
- Modular code structure with separate classes for Books, Users, and Authors
- Reservation system for unavailable books
- Fine calculation system for overdue books

## Project Structure
### Directory Layout
library_mgmt/
    ├── author.py       # Author class implementation
    ├── book.py         # Book class implementation
    ├── user.py         # User class implementation
    ├── library.py      # Main program and menu interface
    ├── books.txt       # Book data storage
    ├── users.txt       # User data storage
    └── authors.txt     # Author data storage

## How to Run
1. Ensure you have Python 3.x installed on your system
2. Clone this repository to your local machine
3. Navigate to the project directory
4. Run the program using:
python library.py

## Features Implemented From Requirements
- Enhanced command-line user interface
- Complete class structure (Book, User, Author)
- Encapsulation using private attributes
- Modular code organization
- File handling for data persistence
- Error handling
- Bonus: Reservation system
- Bonus: Fine calculation

## System Details

### Classes and Functionality

#### Book Class
- Manages individual book information and status
- Tracks borrowing status
- Stores book details (title, author, genre, publication date)
- Handles book borrowing and returning operations
- Provides JSON-based file storage

#### User Class
- Manages library member information
- Tracks borrowed and reserved books
- Calculates late fees
- Handles book reservations
- Manages due dates for borrowed books
- Provides JSON-based file storage

#### Author Class
- Stores author information and biographies
- Manages author-book relationships
- Provides JSON-based file storage

## Future Enhancements
- Implement search functionality by various criteria
- Add unit tests
- Enhance error handling and input validation
- Add administrative features
- Implement database storage instead of text files

## Author
Danielle Bronson  
Coding Temple Python Course  
Date: 2024