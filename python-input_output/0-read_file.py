#!/usr/bin/python3
"""This module contains a function that reads a UTF-8 file and prints it."""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as fie:
        print(file.read, end="")