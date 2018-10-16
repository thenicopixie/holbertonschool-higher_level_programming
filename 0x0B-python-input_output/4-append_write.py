#!/usr/bin/python3
""" Module that appends a string to the end of a text file and
returns the number of characters added"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file
    Args:
        filename - file to append to
        text - text to append
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
