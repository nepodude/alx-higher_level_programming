#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        sys = __import__('sys')
        print("Exception: {}".format(e), file=sys.stderr)
        return False
