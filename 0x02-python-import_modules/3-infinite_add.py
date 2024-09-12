#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv[1:]
args = len(argv)
sum = 0
if args == 0:
    print(0)
elif args > 0:
    for i in range(args):
        sum += int(argv[i])
    print(sum)
