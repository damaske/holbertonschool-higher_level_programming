#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=None):
        if item is None:
        item = len(self) - 1

        popped = super().pop(item)
        print(f"Popped [{item}] from the list.")
        return popped
