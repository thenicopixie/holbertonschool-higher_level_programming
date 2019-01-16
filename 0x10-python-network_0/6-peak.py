#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """go through list to find a peak"""
    nums = list_of_integers
    if nums is None:
        return None
    if len(nums) == 1:
        return nums[0]
    ln = len(nums) - 1
    if ln % 2 != 0:
        ln + 1
    point = int(ln/2)
    l = point - 1
    r = point + 1
    if l >= 0 and r <= ln:
        if nums[point] >= nums[l] and nums[point] >= nums[r]:
            return nums[point]
        else:
            if nums[l] >= nums[point]:
                return find_peak(nums[0:point+1])
            if nums[r] >= nums[point]:
                return find_peak(nums[point:ln+1])
    elif l < 0:
        if r <= ln:
            if nums[point] >= nums[r]:
                return nums[point]
    elif r > ln:
        if l >= 0:
            if nums[point] >= nums[l]:
                return nums[point]
