#!/usr/bin/python3
def safe_print_integer(value):
        try:
            print("{:d}".format(value)) # Will only print if the datatype of 'value' is int
            return True
               
        except Exception:
            return False
