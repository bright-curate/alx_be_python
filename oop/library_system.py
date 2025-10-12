# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Subclass representing an electronic book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """Return details of the EBook."""
        return f"{self.title} by {self.author} [EBook - {self.file_size}MB]"


class PrintBook(Book):
    """Subclass representing a printed book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return details of the PrintBook."""
        return f"{self.title} by {self.author} [PrintBook - {self.page_count} pages]"


class Library:
    """A class representing a library that contains books."""

    def __init__(self):
        self.books = []  # composition: Library has a list of Book objects

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
