#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    s = set(x for x in my_list)
    for i in s:
        sum += i
    return sum
