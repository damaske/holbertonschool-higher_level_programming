#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0 or idx >= len(copy_list):
        return copy_list
    else:
        copy_list[idx] = element
        return my_list, copy_list
