class Book:
    """A class representing a book in a library."""

    def __init__(self, title, author):
        """Initialize a book with a title, author, and checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it's available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        # If book not found, do nothing (main.py doesn't expect an error message)

    def return_book(self, title):
        """Return a book by its title (mark it as available)."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """List all available books (not checked out)."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")