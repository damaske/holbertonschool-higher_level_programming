#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multy = a_dictionary.copy()
    for key in multy:
        multy[key] *= 2
    return multy
