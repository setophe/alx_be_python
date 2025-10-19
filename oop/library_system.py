# library_system.py

class Book:
    """Base class for all book types."""
    def __init__(self, title, author):
        """Initializes a Book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Represents an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook, calling the parent constructor and
        adding the file_size attribute.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a physical book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook, calling the parent constructor and
        adding the page_count attribute.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Represents a library that manages a collection of books,
    demonstrating composition.
    """
    def __init__(self):
        """Initializes the Library with an empty list to hold books."""
        # Composition: The Library class 'has-a' list of Book objects.
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library using its __str__ method."""
        for book in self.books:
            print(book)