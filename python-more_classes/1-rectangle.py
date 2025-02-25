#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """This class defines a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

@property
def width(self):
    return self.width

@width.setter
def width(self, value):
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")

@property
def height(self):
    return self.height

@height.setter
def height(self, value):
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
