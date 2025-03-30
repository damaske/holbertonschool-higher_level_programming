#!/usr/bin/python3
"""This module contains save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON representation."""

    return json.load(my_obj)
