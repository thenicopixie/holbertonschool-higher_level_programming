#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    biggest = 0
    for i in my_list:
        if i > biggest:
            biggest = i
    return (biggest)
