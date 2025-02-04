# Library Management System

A robust Python-based Library Management System that implements enumerations for book genres and membership levels, along with custom exception handling for various error scenarios.

## Features

### 📚 Book Management
- Track books by title and genre
- Monitor book availability status
- Handle book borrowing and returns
- Automated late return detection

### 👥 Membership System
- Multiple membership tiers (Basic, Premium, Gold)
- Tier-specific annual fees
- Automated fee calculation
- Membership validation

### 🎯 Error Handling
- Custom exceptions for various error scenarios
- Graceful handling of edge cases
- Robust input validation
- Detailed error messages

## Project Structure

```
SESSION-24/
├── .github/
├── library_system_modules/
│   ├── __init__.py
│   ├── book_genre.py
│   ├── library_exceptions.py
│   ├── library_system.py
│   ├── library.py
│   ├── member.py
│   └── membership_level.py
├── main.py
├── README.md
└── tests.py
```

## Module Descriptions

- `book_genre.py`: Contains the BookGenre enumeration (FICTION, NON_FICTION, etc.)
- `library_exceptions.py`: Defines custom exceptions for error handling
- `library_system.py`: Core system implementation
- `library.py`: Book-related functionality
- `member.py`: Member class implementation
- `membership_level.py`: MembershipLevel enumeration with fee structure
- `main.py`: Entry point with example usage
- `tests.py`: Unit tests for the system

## Technical Implementation

### Enumerations

#### BookGenre
```python
class BookGenre(Enum):
    FICTION = 1
    NON_FICTION = 2
    SCIENCE = 3
    HISTORY = 4
    BIOGRAPHY = 5
```

#### MembershipLevel
```python
class MembershipLevel(Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500
```

### Custom Exceptions
- `BookNotAvailableError`: Handles attempts to borrow unavailable books
- `InvalidMembershipError`: Manages invalid membership level scenarios
- `LateReturnError`: Processes late book returns

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/library-management-system.git
```

2. Navigate to the project directory:
```bash
cd SESSION-24
```

3. Run the main program:
```bash
python main.py
```

## Usage Example

```python
# Create a new book
book = Book("The Great Gatsby", BookGenre.FICTION)

# Create a new member
member = Member("John Doe", MembershipLevel.PREMIUM)

try:
    # Attempt to borrow a book
    book.borrow()
    
    # Return the book (on time)
    book.return_book(is_late=False)
    
    # Get membership fee
    fee = member.get_fee()
    print(f"Annual fee: ${fee}")
    
except BookNotAvailableError:
    print("Sorry, the book is not available")
except LateReturnError:
    print("Book returned late. Late fees apply")
except InvalidMembershipError:
    print("Invalid membership level")
```

## Testing

Run the test suite:
```bash
python tests.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Project structure inspired by modern Python best practices
- Exception handling patterns based on Python official documentation
- Enumeration implementation following PEP 435