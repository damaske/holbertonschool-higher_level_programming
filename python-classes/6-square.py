#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This class defines a square with a specified size."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size for the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set a new position for the square."""
        if (not isinstance(value, tuple) or 
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' with the given position."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
