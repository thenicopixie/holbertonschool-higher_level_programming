#!/usr/bin/python3
def safe_print_division(a, b):
    diff = None
    try:
        diff = a / b
    except:
        return diff
    finally:
        print("Inside Result: {}".format(diff))
        return diff
