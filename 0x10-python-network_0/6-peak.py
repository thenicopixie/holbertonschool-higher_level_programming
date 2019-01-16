#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """go through list to find a peak"""
    if list_of_integers is None or list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]
    if len(list_of_integers) > 2:
        if ((list_of_integers[len(list_of_integers)//2] > list_of_integers[(
             len(list_of_integers)//2)-1]) and (list_of_integers[len(
               list_of_integers)//2] > list_of_integers[(
                 len(list_of_integers)//2)+1])):
            return list_of_integers[len(list_of_integers)//2]
        else:
            if (list_of_integers[(len(
                list_of_integers)//2)-1] > list_of_integers[(
                  len(list_of_integers)//2)+1]):
                return (find_peak(list_of_integers[0:(
                       len(list_of_integers)//2)+1]))
            else:
                return (find_peak(list_of_integers[len(
                       list_of_integers)//2:len(list_of_integers)+1]))
    else:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
