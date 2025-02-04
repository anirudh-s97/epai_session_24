from library_system_modules.book_genre import BookGenre
from library_system_modules.library_exceptions import BookNotAvailableError, LateReturnError

class Book:
    def __init__(self, title: str, genre: BookGenre, available: bool):
        self.title = title
        self.genre = genre
        self.is_available = available

    def borrow(self):
        if not self.is_available:
            raise BookNotAvailableError(self.title)
        self.is_available = False

    def return_book(self, is_late: bool):
        if is_late:
            raise LateReturnError(self.title, days_late=1)  # days_late=1 is just an example
        self.is_available = True
