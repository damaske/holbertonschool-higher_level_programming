#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i + 1, 10):
     print("{}".format(f"{i}{k}"), end=", " if i < 8 else "\n")
