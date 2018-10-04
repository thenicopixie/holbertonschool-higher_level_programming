#!/usr/bin/python3
"""Module for text_indentation"""

def text_indentation(text):
    """text_indentation - indent and print text according to cases

    Args:
    text - text to indent and print
    """
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{}\n\n".format(i), end="")
            flag = 1
        elif i == " " and flag == 1:
                pass
        else:
            print("{}".format(i), end="")
            flag = 0
