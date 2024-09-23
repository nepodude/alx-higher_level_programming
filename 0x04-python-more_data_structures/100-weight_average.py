#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum_numerator = 0
    sum_weights = 0
    for value, weight in my_list:
        sum_numerator += value * weight
        sum_weights += weight
    return sum_numerator / sum_weights
