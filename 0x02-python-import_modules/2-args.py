#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
number = len(argv)
if number == 1:
    print("0 arguments.")
else:
    if number != 2:
        print("{} arguments:".format(number - 1))
    elif number == 2:
        print("{} argument:".format(number - 1))
    for i in range(1, number):
        print("{}: {}".format(i, argv[i]))
