#!/usr/bin/python3
"""This module contains the is_same_class() function.
    Checks if the object is an instance of the given class."""


def is_same_class(obj, a_class):
    "Returns - bool True if obj is an instance of a_class.
    False if obj is not an instance of a_class o
    if a_class is the object class."

    return isinstance(obj, a_class)
