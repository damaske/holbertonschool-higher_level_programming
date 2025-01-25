#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
            element_div = my_list_1[i] / my_list_2[i]
        else:
            raise IndexError
        except ZeroDivisionError:
            print("division be 0")
            element_div = 0
        except TypeError:
            print("wrong type")
            element_div = 0
        except IndexError:
            print("out of range")
            element_div = 0
        finally:
            result_list.append(element_div)
    return result_list
