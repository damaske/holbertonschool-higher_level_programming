#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_in = my_list[0]
    for i in my_list:
        if i > max_in:
            max_in = i
     return max_in
