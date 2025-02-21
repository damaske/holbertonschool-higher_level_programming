#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This class defines a square with a specified size."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        print("\n" * __self.position[1], end="")
        
        for _ in range(__self.size):
            print(" " * __self.position[0] + "#" * __self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
