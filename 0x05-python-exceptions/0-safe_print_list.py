#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     count = 0
    try:
        for element in my_list:
            if count < x:
                print(element, end='')
                count += 1
            else:
                break
        print()
    except Exception as e:
        print(f"An error occured: {e}")
    return count
