#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newone = my_list.copy()
    for i in range(len(newone)):
            if newone[i] == search:
                newone[i] = replace
    return newone
