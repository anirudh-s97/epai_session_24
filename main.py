from library_system_modules.library_system import Book
from library_system_modules.member import Member
from library_system_modules.book_genre import BookGenre
from library_system_modules.membership_level import MembershipLevel
from library_system_modules.library_exceptions import BookNotAvailableError, InvalidMembershipError, LateReturnError

def main():
    # Create books
    books = [
        Book("The Great Gatsby", BookGenre.FICTION),
        Book("A Brief History of Time", BookGenre.SCIENCE),
        Book("The Diary of Anne Frank", BookGenre.BIOGRAPHY)
    ]

    # Create members
    try:
        members = [
            Member("John Doe", MembershipLevel.BASIC),
            Member("Jane Smith", MembershipLevel.PREMIUM),
            Member("Bob Johnson", MembershipLevel.GOLD)
        ]

        # Test membership fees
        for member in members:
            print(f"{member.name}'s annual fee: ${member.get_fee()}")

        # Test book borrowing
        print("\nTesting book borrowing:")
        books[0].borrow()
        print(f"Successfully borrowed: {books[0].title}")

        # Try to borrow the same book again
        try:
            books[0].borrow()
        except BookNotAvailableError as e:
            print(f"Error: {e}")

        # Test book returning
        print("\nTesting book returning:")
        # Normal return
        books[0].return_book(is_late=False)
        print(f"Successfully returned: {books[0].title}")

        # Late return
        try:
            books[1].borrow()
            books[1].return_book(is_late=True)
        except LateReturnError as e:
            print(f"Error: {e}")

        # Test invalid membership
        try:
            invalid_member = Member("Invalid", "INVALID_LEVEL")
        except InvalidMembershipError as e:
            print(f"\nError: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()