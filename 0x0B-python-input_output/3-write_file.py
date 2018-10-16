#!/usr/bin/python3
""" Module that writes a string to a test file and returns the number
of character written"""


def write_file(filename="", text=""):
    """Write a string to a file. Return the number of
    characters written.
    Args:
        filename - file to write to
        text - text to write in file
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
