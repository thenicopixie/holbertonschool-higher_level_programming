#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        dig = number % 10
    elif number < 0:
        dig = number % -10
        dig *= -1
    print("{:d}".format(dig), end="")
    return (dig)
