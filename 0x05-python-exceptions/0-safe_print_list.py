#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    howmany = 0
    for i in my_list:
        howmany += 1
    try:
        i = 0
        for element in my_list:
            if i != x - 1 and x != 0:
                print(element, end='')
            if i == x - 1 or i == howmany - 1:
                print(element)
            i += 1
            if i == x:
                break
        return i
    except Exception as e:
        print(f"An error occured: {e}")
