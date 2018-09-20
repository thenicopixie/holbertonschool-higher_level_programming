#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def func(sub_list):
        return list(map(lambda x: x**2, sub_list))
    return list(map(func, matrix))
