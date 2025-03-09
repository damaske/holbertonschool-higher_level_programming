#!/usr/bin/python3
"""This class contains class named Square(Rectangle)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """nstantiation with size"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        Rectangle.__init__(self, width=self.__size, height=self.__size)
