class Book:
    """
    A class to represent a Book with a title, author, and publication year,
    implementing various Python magic methods.
    """

    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed.
        Prints a message including the book's title.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method, used by print() and str().
        Returns a user-friendly string format.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation method, used by repr().
        Returns a string that can be used to recreate the object.
        """
        # Note: Strings are enclosed in quotes, the integer year is not.
        return f"Book('{self.title}', '{self.author}', {self.year})"