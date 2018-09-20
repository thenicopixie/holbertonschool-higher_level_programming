#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    new_dict.update((key, val * 2) for key, val in a_dictionary.items())
    return new_dict
