#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        duplicate = [item for item in my_list]
        total = 0
        length = len(duplicate)
        for i in range(length):
            for item in duplicate:
                total += item
            average = total / len(duplicate)
            duplicate = [x for x in duplicate if x >= average]
    return duplicate[0]
