#!/usr/bun/python3

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (r ** 2)
    def perimeter(self):
        return math.pi * 2 * radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(Shape):
    a = Shape.area()
    p = Shape.perimeter()
    print("Area: {}".format(a))
    print("Perimeter: {}".format(p))
