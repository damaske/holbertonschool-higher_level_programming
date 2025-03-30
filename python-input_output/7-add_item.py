#!/usr/bin/python3
"""This module contains script that
adds all arguments to a Python list,
and then save them to a file."""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if os.path.exists("./add_item.json"):
    list_arg = load_from_json_file("add_item.json")
else:
    list_arg = []

save_to_json_file(list_arg + sys.argv[1:], "add_item.json")
