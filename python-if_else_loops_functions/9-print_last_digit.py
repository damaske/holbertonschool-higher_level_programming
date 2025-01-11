#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    last_dig = abs(number) % 10
    print(last_dig, end="")
    return(last_dig)

