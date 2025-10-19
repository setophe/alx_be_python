class Book:

    def __init__(self, title : str, author : str , year : int):
        self._title = title
        self._author = author
        self._year = year

    def __del__(self):
        print(f"Deleting {self._title}")

    def __str__(self):
        return f"{self._title} by {self._author}, published in {self._year}"

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', {self._year})"