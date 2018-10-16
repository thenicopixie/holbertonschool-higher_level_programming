#!/usr/bin/python3
""" Return the numbers of lines of a text file """


def number_of_lines(filename=""):
    """Function that returns the number of lines in a file
    Args:
        filename - file to read
    """
    with open(filename, encoding="utf-8") as a_file:
        line_count = 0
        for a_line in a_file:
            line_count += 1
        return line_count
