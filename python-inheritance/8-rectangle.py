#!/usr/bin/python3
"""This class contains class named Rectangle(BaseGeometry):"""


class Rectangle(BaseGeometry):
    """nstantiation with width and height"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
