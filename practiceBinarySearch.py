# -*- coding: utf-8 -*-
"""
    Author: Rick Sam
    Date: September 27
    Program: Binary Search
    Comments: Frustrated on Algorithms -_- However, I was thinking of relying on God and not on myself,
    sounds silly but think about this, What if tomorrow you don't wake up? I mean, we live our life as
    if nothing will happen to us. I was thinking of all great thinkers, like Doestoevesky. Every day,
    we wake up and do things but then what's the meaning of doing all these?

    ""Example: seq = [10,9,8,6,5,4,3,2,1]
    In this, I want to find 1
    So Binary Search, First, I define a function and give two arguments
    I find the mid point.... which is len(seq)//2
    min = 0
    max = len(seq) - 1, which is 8
"""
def binary_search(seq, t):
    min = 0
    max = len(seq) - 1 # 8
    while True: # Okay
        if max < min: # 7 < 0?
            return -1
        elif seq[mid] < t: #
            min = mid + 1
        elif seq[m] > t:
            max = mid - 1
        else:
            return mid

if __name__ == '__main__':
    seq = [10,9,8,6,5,4,3,2,1]
    binary_search(seq, 1)

"""
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1


def binary_search(l, value, low = 0, high = -1):
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low >= high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search(l, value, low, mid-1)
    elif l[mid] < value: return binary_search(l, value, mid+1, high)
    else: return mid

    """
