#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Will only print if the datatype of 'value' is int
        print("{:d}".format(value))
        return True

    except Exception:
        return False
