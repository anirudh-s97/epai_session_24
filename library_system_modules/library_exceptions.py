class BookNotAvailableError(Exception):
    """Raised when a requested book is not available for borrowing"""
    def __init__(self, book_title):
        self.message = f"The book '{book_title}' is not available for borrowing"
        super().__init__(self.message)

class InvalidMembershipError(Exception):
    """Raised when an invalid membership level is referenced"""
    def __init__(self, membership_level):
        
        self.message = f"Invalid membership level: {membership_level}"
        super().__init__(self.message)

class LateReturnError(Exception):
    """Raised when a book is returned after its due date"""
    def __init__(self, book_title, days_late):
        self.message = f"The book '{book_title}' is {days_late} days overdue"
        super().__init__(self.message)