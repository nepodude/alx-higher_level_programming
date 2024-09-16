#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        current_max = my_list[0]
        for number in my_list:
            if number > current_max:
                current_max = number
    return current_max
