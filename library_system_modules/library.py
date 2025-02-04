from datetime import datetime, timedelta
from library_system_modules.book_genre import BookGenre
from library_system_modules.membership_level import MembershipLevel
from library_system_modules.library_exceptions import BookNotAvailableError, InvalidMembershipError, LateReturnError
from library_system_modules.library_system import Book
from library_system_modules.member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title: str, genre: BookGenre):
        self.books.append(Book(title, genre))

    def add_member(self, name: str, membership_level: MembershipLevel):
        member = Member(name, membership_level)
        self.members.append(member)
        return member

    def borrow_book(self, member: Member, book_title: str):
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book or not book.is_available:
            raise BookNotAvailableError(book_title)

        book.is_available = False
        book.due_date = datetime.now() + timedelta(days=14)  # 2-week lending period
        member.borrowed_books.append(book)

    def return_book(self, member: Member, book_title: str):
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        
        if not book:
            raise ValueError(f"Member has not borrowed book: {book_title}")

        if datetime.now() > book.due_date:
            days_late = (datetime.now() - book.due_date).days
            raise LateReturnError(book_title, days_late)

        book.is_available = True
        book.due_date = None
        member.borrowed_books.remove(book)