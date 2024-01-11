#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        # Will only print if the datatype of 'value' is int
        print("{:d}".format(value))
        return True

    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return False
