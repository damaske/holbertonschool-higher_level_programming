#!/usr/bin/python3
"""This module contains save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object
    to a text file, using a JSON representation."""

    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
