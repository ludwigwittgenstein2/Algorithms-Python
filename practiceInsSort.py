# -*- coding: utf-8 -*-
"""
Author: Rick Sam
Book: Algorithms Python
Date: September 29, 2016
"""


def ins_sort(seq):
    """This is DocString –– Insertion sort function for file."""
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -=1
    print seq
    print ins_sort.__doc__

if __name__ == '__main__':
    seq = [10,9,8]
    ins_sort(seq)
