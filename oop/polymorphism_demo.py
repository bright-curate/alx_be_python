# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Calculate the area of the shape (to be implemented by subclasses)."""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
