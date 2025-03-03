#!/usr/bin/python3
"""A subclass of list that includes a method
to print the list in sorted order."""


class MyList(list):
    """Prints the list elements in ascending sorted order.
    This method does not modify the original list; it only prints a sorted copy."""

    def print_sorted(self):
        print(sorted(self))
        return sorted(self
