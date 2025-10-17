class book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    #Attributes
    def __init__(self):
        self._books = []

    #Methods
    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                self._is_checked_out = True
                print(f"the book {book.title} is checked out")
                return
            else:
                print(f"the book {book.title} is already checked out")
                return
        print(f"the book {title} is not found in the library")

    def retur_book_title(self,title):
        for book in self._books:
            if book.title == title:
                book.is_checked_out = False
                return
            else:
                print(f"the book {book.title} is not checked out")
                return

    def lis_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]

        if not available_books:
            print("No available books in the library.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")

