#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print("Added {item} to the list.")

    def extend(self, item):
        super().extend(item)
        print("Extended the list with {x} items.")

    def remove(self, item):
        super().remove(item)
        print("Removed {item} from the list.")

    def pop(self, item):
        print("Popped {item} from the list.")
