#!/usr/bin/python3
"""This module contains a function that reads a UTF-8 file and prints it."""

def read_file(filename=""):
"""Function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode="r", encoding="utf-8") as fie:
        print(file.read, end="")