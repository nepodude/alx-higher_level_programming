#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in my_list:
        if i < x:
            try:
                print("{:d}".format(j), end='')
                i += 1
            except Exception as e:
                continue
    print()
    return i
