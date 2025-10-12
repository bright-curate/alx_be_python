# book_class.py

class Book:
    """A class to represent a book."""

    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Print a message when the object is deleted."""
        print(f"Deleting {self.title}")

    
