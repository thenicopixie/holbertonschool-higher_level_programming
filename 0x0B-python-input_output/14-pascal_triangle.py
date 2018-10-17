#!/usr/bin/python3
"""Creates Pascal's Triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal's
    triangle of n"""
    a_list = []
    if n <= 0:
        return a_list
    a_list.append([1])
    if n == 1:
        return a_list
    a_list.append([1, 1])
    if n == 2:
        return a_list
    for i in range(2, n):
        b_list = []
        for x in range(i + 1):
            print(b_list)
            print(i)
            print(x)
            if x > 0 and x <= i - 1:
                b_list.append(a_list[i - 1][x - 1] + a_list[i - 1][x])
            else:
                b_list.append(1)
        a_list.append(b_list)
    return a_list
