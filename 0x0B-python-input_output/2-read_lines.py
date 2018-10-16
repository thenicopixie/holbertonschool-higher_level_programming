#!/usr/bin/python3
""" Module that reads n lines of a test file and prints to stdout """


def read_lines(filename="", nb_lines=0):
    """ Read n lines from a file and print to stdout
    Args:
        filename - file to read
        nb_lines - number of lines to read
    """
    with open(filename, encoding="utf-8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            line_count = 0
            for a_line in a_file:
                if line_count != nb_lines:
                    print(a_line, end="")
                    line_count += 1
                else:
                    break
