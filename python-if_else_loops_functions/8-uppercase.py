#!/usr/bin/python3
def uppercase(str):
    for lett in str:
        if 'a' <= lett <= 'z':
            lett = chr(ord(lett) - 32)
        print("{}".format(f"{lett}"), end="")
    print()
