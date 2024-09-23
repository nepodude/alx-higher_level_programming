#!/usr/bin/python3
dictionary = {"Nepo": 21, "Jean": 22, 'Munezero': 20}
my_age = 21
for name, age in dictionary.items():
    if age == my_age:
        print("{}'s age is{}".format(name, age), end='.......')
    