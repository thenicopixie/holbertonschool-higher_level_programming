#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    product = 0
    add = 0
    for i in range(len(my_list)):
        product += my_list[i][0] * my_list[i][1]
        add += my_list[i][1]
    return (product / add)
