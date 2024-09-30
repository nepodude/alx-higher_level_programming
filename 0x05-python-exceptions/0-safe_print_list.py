#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line.

    Args:
        my_list (list): The list to print from.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements actually printed.
    """
    count = 0
    try:
        if x < 0:
            print("Error: x cannot be negative.")
            return count
        for element in my_list:
            if count < x:
                print(element, end='')
                count += 1
            else:
                break
        print()  # Print newline after printing elements
    except TypeError:
        print("Error: my_list is not iterable.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return count
