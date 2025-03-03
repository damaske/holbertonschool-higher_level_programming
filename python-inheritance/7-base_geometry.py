#!/usr/bin/python3
"""This class contains class named BaseGeometry"""


class BaseGeometry:
    """method area"""

    def area(self):
        """Exception area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
