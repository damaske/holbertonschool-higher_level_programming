#!/usr/bin/python3

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Represents a circle with a given radius."""
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        return pi * (self.radius ** 2)
    def perimeter(self):
        return pi * 2 * self.radius

class Rectangle(Shape):
    """Represents a rectangle with width and height."""
    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """Print the area and perimeter of a shape."""
    a = shape.area()
    p = shape.perimeter()
    print("Area: {}".format(a))
    print("Perimeter: {}".format(p))
