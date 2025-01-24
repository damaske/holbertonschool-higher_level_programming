#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = []
    for element in my_list:
        if element not in set_list:
            set_list.append(element)
    return sum(set_list)
