#!/usr/bin/python3

"""A function to print sorted list made of integers"""


class MyList(list):
    """Start printing by creating a method inside which will
    print the elements from a list we inherited from"""
    def print_sorted(self):
        """Create a list which is sorted"""
        my_list = sorted([
            element for element in self if isinstance(element, int)
            ])
        print(my_list)
