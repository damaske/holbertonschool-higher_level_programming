#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        My_d = {}
        for key in attrs:
            if key in self.__dict__:
                My_d[key] = self.__dict__[key]
        return My_d

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if not len(json) is 0:
            self.__dict__ = json
